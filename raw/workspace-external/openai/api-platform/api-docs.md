---
source_url: https://developers.openai.com/api/docs
vendor: openai
topic: api-platform
fetched_at: 2026-06-10T07:11:44Z
revalidate_after: 2026-09-08T07:11:44Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:openai
authority: standard
ingest_mode: defuddle
---

## API Platform

## Developer quickstart

Make your first API request in minutes. Learn the basics of the OpenAI platform.

```javascript
import OpenAI from "openai";
const client = new OpenAI();

const response = await client.responses.create({
  model: "gpt-5.5",
  input: "Write a short bedtime story about a unicorn.",
});

console.log(response.output_text);
```

## Models

Start with GPT-5.5 for complex reasoning and coding, or choose GPT-5.4 mini and GPT-5.4 nano for lower-latency, lower-cost workloads.

[View all](https://developers.openai.com/api/docs/models)

## Start building[Read and generate text](https://developers.openai.com/api/docs/guides/text)

[

Use the API to prompt a model and generate text

](https://developers.openai.com/api/docs/guides/text)[

Use a model's vision capabilities

Allow models to see and analyze images in your application

](https://developers.openai.com/api/docs/guides/images-vision)[

Generate images as output

Create images with GPT Image 2

](https://developers.openai.com/api/docs/guides/image-generation)[

Build apps with audio

Analyze, transcribe, and generate audio with API endpoints

](https://developers.openai.com/api/docs/guides/audio)[

Build agentic applications

Use the API to build agents that use tools and computers

](https://developers.openai.com/api/docs/guides/agents)[

Achieve complex tasks with reasoning

Use reasoning models to carry out complex tasks

](https://developers.openai.com/api/docs/guides/reasoning)[

Tailor to your use case

Adjust our models to perform specifically for your use case with fine-tuning, evals, and distillation

](https://developers.openai.com/api/docs/guides/model-optimization)