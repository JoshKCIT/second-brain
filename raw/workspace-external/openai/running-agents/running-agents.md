---
source_url: https://developers.openai.com/api/docs/guides/agents/running-agents
vendor: openai
topic: running-agents
fetched_at: 2026-06-10T07:11:48Z
revalidate_after: 2026-09-08T07:11:48Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:openai
authority: standard
ingest_mode: defuddle
---

Defining an agent is only the setup step. The runtime questions are what a single run does, how the next turn continues, and how the workflow behaves when it pauses for approvals or tool work.

## The agent loop

One SDK run is one application-level turn. The runner keeps looping until it reaches a real stopping point:

1. Call the current agent’s model with the prepared input.
2. Inspect the model output.
3. If the model produced tool calls, execute them and continue.
4. If the model handed off to another specialist, switch agents and continue.
5. If the model produced a final answer with no more tool work, return a result.

That loop is the core concept behind the SDK. Tools, handoffs, approvals, and streaming all build on top of it rather than replacing it.

## Choose one conversation strategy

There are four common ways to carry state into the next turn:

| Strategy | Where state lives | Best for | What you pass on the next turn |
| --- | --- | --- | --- |
| `result.history` | Your application | Small chat loops and maximum control | The replay-ready history |
| `session` | Your storage plus the SDK | Persistent chat state, resumable runs, and storage you control | The same session |
| `conversationId` | OpenAI Conversations API | Shared server-managed state across workers or services | The same conversation ID and only the new turn |
| `previousResponseId` | OpenAI Responses API | The lightest server-managed continuation from one response to the next | The last response ID and only the new turn |

In most applications, pick one strategy per conversation. Mixing local replay with server-managed state can duplicate context unless you are deliberately reconciling both layers.

```typescript
import { Agent, MemorySession, run } from "@openai/agents";

const agent = new Agent({
  name: "Tour guide",
  instructions: "Answer with compact travel facts.",
});

const session = new MemorySession();

const firstTurn = await run(
  agent,
  "What city is the Golden Gate Bridge in?",
  { session },
);
console.log(firstTurn.finalOutput);

const secondTurn = await run(agent, "What state is it in?", { session });
console.log(secondTurn.finalOutput);
```

Sessions are the best default when you want durable memory, resumable approval flows, or storage that your application controls.

```typescript
import { Agent, run } from "@openai/agents";
import OpenAI from "openai";

const agent = new Agent({
  name: "Assistant",
  instructions: "Reply very concisely.",
});

const client = new OpenAI();
const { id: conversationId } = await client.conversations.create({});

const first = await run(agent, "What city is the Golden Gate Bridge in?", {
  conversationId,
});
console.log(first.finalOutput);

const second = await run(agent, "What state is it in?", {
  conversationId,
});
console.log(second.finalOutput);
```

Use `conversationId` when multiple systems should share one named conversation. Use

`previousResponseId`

when you want the cheapest response-to-response continuation option.

## Stream runs incrementally

Streaming uses the same agent loop and the same state strategies. The only difference is that you consume events while the run is still happening.

```typescript
import { Agent, run } from "@openai/agents";

const agent = new Agent({
  name: "Planet guide",
  instructions: "Answer with short facts.",
});

const stream = await run(agent, "Give me three short facts about Saturn.", {
  stream: true,
});

for await (const event of stream) {
  if (
    event.type === "raw_model_stream_event" &&
    event.data.type === "response.output_text.delta"
  ) {
    process.stdout.write(event.data.delta);
  }
}

await stream.completed;
console.log("\nFinal:", stream.finalOutput);
```

Three practical rules matter:

- Wait for the stream to finish before treating the run as settled.
- If the run pauses for approval, resolve `interruptions` and resume from `state` rather than starting a fresh user turn.
- If you cancel a stream mid-turn, resume the unfinished turn from `state` if you want the same turn to continue later.

## Handle pauses and failures deliberately

Two broad classes of non-happy-path outcomes matter:

- **Runtime or validation failures** such as max-turn limits, guardrail exceptions, or tool errors.
- **Expected pauses** such as human approval requests, where the run is intentionally interrupted and should later resume from the same state.

Treat approvals as paused runs, not as new turns. That distinction keeps turn counts, history, and server-managed continuation IDs consistent.

## Next steps

Once the runtime loop is clear, move to the guide that matches the next workflow boundary you need to design.[Results and state](https://developers.openai.com/api/docs/guides/agents/results)

[

Learn which result surfaces your application should carry into the next turn.

](https://developers.openai.com/api/docs/guides/agents/results)[

Orchestration and handoffs

Decide how multiple specialists behave inside the same runtime loop.

](https://developers.openai.com/api/docs/guides/agents/orchestration)[

Guardrails and human review

Add validation and approval pauses without breaking turn continuity.

](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals)