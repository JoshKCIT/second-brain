---
source_url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-generative-actions
vendor: microsoft-copilot-studio
topic: generative-orchestration
fetched_at: 2026-06-10T07:02:48Z
revalidate_after: 2026-09-08T07:02:48Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:microsoft-copilot-studio
authority: standard
ingest_mode: defuddle
---

## Orchestrate agent behavior with generative AI

Agents can use either generative or classic orchestration. By default, newly created agents use generative orchestration. An agent that uses generative orchestration can choose the best [tools](https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-tools-custom-agent), [knowledge](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-studio), [topics](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-create-edit-topics), and [other agents](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-add-other-agents) to answer user queries or respond to event triggers. The alternative is classic orchestration, where an agent responds to users by triggering the topic whose trigger phrases most closely match the user's query.

Important

- If you create an agent from a prebuilt agent, the prebuilt agent's configuration determines which orchestration method the agent uses.
- If an admin turns off the ability to use generative orchestration in an environment, agents created in that environment can only use classic orchestration.

The following table compares agent behavior between generative orchestration and classic orchestration.

| Behavior | Generative orchestration | Classic orchestration |
| --- | --- | --- |
| Topics | The agent selects topics based on the description of their purpose. | The agent selects topics based on matching a user query with trigger phrases. |
| Child and connected agents | The agent selects child and connected agents based on their description. | Not applicable. |
| Tools | The agent can choose to call tools based on their name and description. | Tools can only be called explicitly from within a topic. |
| Knowledge | The agent can choose to proactively search knowledge to answer a user's query. | Knowledge can be used as a fallback when no topics match a user's query (or called explicitly from within a topic). |
| Use of multiple topics, tools, knowledge sources | The agent can use a combination of topics, tools, and knowledge. | The agent tries to select a single topic to respond to the user, falling back to knowledge if configured. |
| Asking users for input | The agent can automatically generate questions to prompt users for any missing information required to fill inputs for topics and tools. | You must use question nodes in topics to author messages prompting the user for any required information. |
| Responding to a user | The agent automatically generates a response, using the available information from topics, tools, other agents, and knowledge that it used. | You must use message nodes in topics to author messages responding to the user (or call a tool from a topic). |

Tip

There are key differences between classic and generative orchestration, such as how knowledge is searched and the supported data sources. Before turning on generative mode for an existing agent, read about the [known limitations](#known-limitations-for-generative-orchestration).

## How does generative orchestration work?

Using generative AI to determine how your agent responds can make the conversation more natural and fluid for the user. An agent that uses generative AI can also perform actions autonomously.

### Selecting the right topics, tools, other agents, and knowledge sources

Note

When your agent determines how to respond to a user message or event, it can use previous [conversation history](#controlling-conversation-history) and context to influence its decisions. This behavior explains that you might see different responses for the same query between a fresh conversation and an ongoing conversation. For example, between a new test conversation in the Copilot Studio [test panel](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-test-bot) and a longer running conversation in Microsoft Teams, which has previous messages. This behavior is expected and allows your agent to respond to follow-up questions or avoid asking for information that it already has.

When a user sends a message, your agent selects one or more tools, topics, other agents, or knowledge sources to prepare its response. Multiple factors determine the selection. The most important factor is the description of the topics, tools, agents, and knowledge sources. Other factors include the name of a topic, tool, agent, or knowledge source, any input or output parameters, and their names and descriptions. Descriptions make it possible for your agent to be more accurate when it associates the user intent with tools, other agents, and topics. You don't need to predict all of the ways a user might indicate what they need.

When you configure an agent to use generative orchestration, it can select one or more tools, topics, other agents, or knowledge sources to handle user queries (including multi-intent queries), or to autonomously respond to events. If the agent selects multiple tools, agents, or topics, it calls them in sequence, after generating any questions to ask the user for missing information.

Learn more about [how agents search across knowledge sources](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-studio) when generative orchestration is turned on.

### Responding to user input or event triggers

The agent takes the information returned from all knowledge sources, tools, agents, and topics that it selected in response to user input or to an event trigger, and summarizes an answer to any originating user query.

Tip

Since an agent configured with generative orchestration can use information from knowledge, tools, other agents, and topics to generate a response, you can make your topics more flexible by not sending their final response in a message node, but instead returning it as an output variable to the agent. This method lets your agent provide contextual responses to your users. Learn more about [configuring topic inputs and outputs](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-managing-topic-inputs-outputs).

### Testing

When you test an agent that uses generative orchestration in Copilot Studio, you can [open the activity map](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-review-activity#real-time-activity-map-during-testing) to follow how your agent is responding.

## Turn off generative orchestration for an agent

1. Go to the **Settings** page for your agent.
2. In the **Generative AI** section, under **Orchestration**, for **Use generative AI orchestration for your agent's responses?**, select **No**. Your agent is now configured to use classic orchestration.

## Turn on generative orchestration for an agent

1. Go to the **Settings** page for your agent.
2. In the **Generative AI** section, under **Orchestration**, for **Use generative AI orchestration for your agent's responses?**, select **Yes**.

Tip

It's a good practice to inform your users that some of the conversation (for example, questions generated when running a tool) might be generated by AI. For example, you could add an extra message in the **Conversation Start** [system topic](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-system-topics), which controls the message shown to your users when a new conversation is started with the agent.

## Authoring descriptions

If you configure an agent to use generative orchestration, provide a high-quality description for each of its child agents, connected agents, topics, tools, and knowledge sources. Good descriptions ensure the agent selects the right topics, tools, other agents, and knowledge sources to respond to users.

For tools, authoring a description is part of the wizard used to add them to the agent. The description is often prepopulated for you, but you can make changes as appropriate. To learn more about adding and managing tools, see [Add tools to custom agents](https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-tools-custom-agent).

For topics, once you turn on generative orchestration, **The agent chooses** appears on **Trigger** nodes (instead of **User says a phrase**), which allows you to add or edit the description for the topic.

Tip

If you turn on generative orchestration for an agent that you initially authored to use classic orchestration, Copilot Studio automatically generates a default description for each existing topic, based on the topic's trigger phrases. The generated description is often good enough to allow these topics to be selected in response to relevant user queries. However, it's a good practice to follow the advice provided in this article to revise the generated descriptions.

## Multilingual support with generative orchestration

For an agent that uses generative orchestration, any content it generates is in the currently active language—either the agent's primary language or one of its secondary languages. The agent automatically determines the user language from the client or browser language. For more information about adding languages for your agent, see [Configure and create multilingual agents](https://learn.microsoft.com/en-us/microsoft-copilot-studio/multilingual). For the list of languages supported with generative orchestration, see [Language support](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-language-support#generative-answers-and-orchestration-and-user-language).

## Best practices

Use the following best practices for naming topics, tools, and knowledge sources. Also use them for drafting clear, concise, and relevant descriptions for these elements.

Tip

If multiple topics have similar descriptions, your agent might invoke them all to answer a question. To prevent this behavior, test your agent thoroughly and revise any overlapping descriptions. Learn more in [Configure high-quality instructions for generative orchestration](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/generative-mode-guidance).

### Writing style

Use simple and direct language. Avoid jargon, slang, or technical terms.

Use the active voice and the present tense for descriptions. For example, write "This tool provides weather information" instead of "Weather information is provided by this tool."

Use bulleted and numbered lists to clearly separate a series of items, actions, or considerations.

### Relevance

Use keywords that relate to the functionality of the tool or topic, and the user's intent. For example, if a tool provides weather information, use keywords like "weather," "forecast," "temperature," "rain," "snow," and so on.

For the description, write a short and informative summary of the tool's or topic's functionality. Limit the summary to one or two sentences. Explain what the tool or topic does and how it benefits the user.

Use a descriptive and unique name that's a short phrase. Avoid using generic or ambiguous names that could be confusing. For example, instead of naming a tool "Weather," name it "Weather Forecast" or "Weather Report."

Use specific language to prevent ambiguity between similar topics and tools.

For example, if your agent already has a tool that provides information about current weather conditions, but you want to add another topic to provide the weather forecast for tomorrow, make sure the names and descriptions of these topics are specific enough to avoid ambiguity. Make sure such similar topics have a different name and description. It can also help to indicate what they can't do. Here are examples of names and descriptions you might use.

Name: Current Weather

Description: This topic provides weather forecast for any location in the world. You can ask for the current weather, including temperature and if it's raining or snowing. It doesn't get weather forecasts for future days.

Name: Weather Forecast for Tomorrow

Description: This topic provides weather information for any location in the world for the next day. It provides the temperature. It doesn't get the current weather for today.

### Examples of what not to do

The following examples don't follow the guidelines. The first example is too vague because it doesn't specify what types of questions the tool can answer.

Name: Answer Question

Description: This tool can answer questions.

The next example uses jargon. Instead, it should spell out earnings per share (EPS).

Name: Get EPS

Description: Gets EPS for any stock ticker.

## Examples of interactions with an agent using generative orchestration to handle user requests

The following examples are based on an agent that has two custom topics—one for finding store hours and another for locating a nearby store—and a tool based on the prebuilt MSN Weather connector.

### Example 1

In this example, the user asks, "What is the weather like in Seattle?". The agent selects the current weather tool and also prepopulates the Location input with "Seattle," which it recognized from the user's question.

![Screenshot of example 1, showing the weather tool on the activity map.](https://learn.microsoft.com/en-us/microsoft-copilot-studio/media/advanced-generative-actions/example-1.png)

Screenshot of example 1, showing the weather tool on the activity map.

### Example 2

In this example, the user says, "I need to get store hours and find my nearest store." The agent selects two items, the **Store Hours** topic and the **Store Locator** topic, and chains them together to respond to both parts of the user's query.

![Screenshot of example 2, showing details from second of two topics chained together on the activity map.](https://learn.microsoft.com/en-us/microsoft-copilot-studio/media/advanced-generative-actions/example-2a.png)

Screenshot of example 2, showing details from second of two topics chained together on the activity map.

### Example 3

In this example, the user finds their nearest store, which is identified as Kirkland, earlier within the conversation. The user then asks, "what's the weather like there?". Here, the agent selects the current weather tool but prepopulates the location with "Kirkland," based on the recent conversation context.

![Screenshot of example 3, showing the conversation history and the weather tool on the activity map.](https://learn.microsoft.com/en-us/microsoft-copilot-studio/media/advanced-generative-actions/example-3.png)

Screenshot of example 3, showing the conversation history and the weather tool on the activity map.

## More control options for generative orchestration

### Canceling the current plan

Use the **End all topics** node within a topic to cancel any remaining steps the orchestrator planned to respond to a user or an event trigger.

### Using topic triggers and controlling use of conversation history

Use either of the following topic triggers to determine an agent's behavior:

- **AI response generated**, when the agent generates a response to a user.
- **Plan complete**, when a plan is completed (that is, when the agent performed all steps to respond to a user).

Learn more about these and other [topics triggers](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-triggers).

### Controlling conversation history

Agents use recent conversation history when making decisions about how to respond to a user or when carrying out other actions, such as generating responses or filling input values from available context. Some channels, such as Microsoft Teams, maintain extensive conversation history by design. If you want your agent to support restarting conversations from a clean slate, set it up to clear the conversation history used by the planner at any time by using a **Clear variable values** node, with the option **Conversation history for the current session**.

Note

By default, the [Reset Conversation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-system-topics#reset-conversation) system topic *doesn't* clear the conversation history. It only clears the global variables for the current session.

## Known limitations for generative orchestration

The following known issues and limitations exist when using the generative orchestration mode.

### Knowledge

With generative orchestration turned on, an agent doesn't use the [Conversational boosting](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-system-topics) system topic when it searches knowledge sources. Therefore, the agent doesn't use any modifications you make to this system topic to customize how it searches knowledge. This limitation also applies to classic data sources configured in generative answers nodes, including custom data sources. Learn more about [how knowledge works with generative orchestration](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-studio#knowledge-search-in-classic-and-generative-modes).

### Custom entity support for topic and tool input parameters

Tools and topics don't yet support custom entities (closed lists and regex entities) as input parameters. To collect information by using a custom entity, use a **Question** node in a topic.

### Disambiguation

An agent might fail to disambiguate between topics when more than one topic closely matches a user's intent. Normally, the agent asks the user to choose between one or more topics that match their intent through the [Multiple Topics Matched](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-system-topics) system topic. However, agents that use generative orchestration currently don't call this topic. If you leave the **Multiple Topics Matched** system topic turned on, your agent starts disambiguating between topics automatically when this problem is resolved. To prevent your agent from automatically disambiguating between topics in the future, turn off the **Multiple Topics Matched** system topic. Turning off this topic allows you to test your agent. You can opt back in to using disambiguation by turning the topic back on after testing your agent.

### Previous conversation context

An agent that uses generative orchestration has access to the recent conversation with the user, which provides context for making decisions about which tools to call or filling inputs with values. The amount of conversation history is currently limited, which means that sometimes the agent can't see or use the information in earlier parts of the conversation. In these cases, it might be necessary to collect some information again from the user, or ensure that key information is included in the transcript at regular intervals.

### Hyperlinks from knowledge source data

Hyperlinks found in knowledge sources such as Word documents, PDF files, or web pages appear as plain text in agent responses.