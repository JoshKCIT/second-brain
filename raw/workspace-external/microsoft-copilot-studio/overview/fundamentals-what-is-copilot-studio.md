---
source_url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio
vendor: microsoft-copilot-studio
topic: overview
fetched_at: 2026-06-10T07:02:47Z
revalidate_after: 2026-09-08T07:02:47Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:microsoft-copilot-studio
authority: standard
ingest_mode: defuddle
---

## Copilot Studio overview

Copilot Studio is a graphical, low-code tool for building agents and agent flows.

![Screenshot of the Copilot Studio Home page.](https://learn.microsoft.com/en-us/microsoft-copilot-studio/media/fundamentals-what-is-copilot-studio/home-page.png)

Screenshot of the Copilot Studio Home page.

One of the standout features of Copilot Studio is its ability to connect to other data sources by using prebuilt or custom connectors. With this flexibility, you can create and orchestrate sophisticated logic, ensuring that your agent experiences are powerful and intuitive.

The platform's low-code experience puts the power of AI at your fingertips, making it accessible even if you don't have an extensive technical background.

## What is an agent?

An agent is a powerful AI companion that can handle a range of interactions and tasks. It can resolve problems that require complex conversations and autonomously determine the best action to take based on its instructions and context. It coordinates language models, along with instructions, context, knowledge sources, topics, tools, inputs, and triggers to accomplish your goals.

Agents can engage with customers and employees in multiple languages across websites, mobile apps, Facebook, Microsoft Teams, or any channel supported by the Azure Bot Service. They can also improve productivity by performing tasks as part of a conversation or in reaction to a trigger to assist users and organizations.

You can easily create agents in Copilot Studio without the need for data scientists or developers. Some of the ways you might use agents include:

- Sales help and support issues
- Opening hours and store information
- Employee health and vacation benefits
- Public health tracking information
- Common employee questions for businesses

Use agents on their own or to extend Microsoft 365 Copilot with enterprise data and scenarios.

[Try the Copilot Studio agent demo](https://copilotstudio.microsoft.com/tryit?azure-portal=true)

## What is a flow?

Flows provide a way to automate repetitive tasks and integrate your apps and services. You can trigger flows manually, by other automated events or agents, or based on a schedule.

With Copilot Studio, you can create flows using natural language or a visual designer. There are two approaches to creating flows:

- Agent flows: The existing flows format in Copilot Studio. Agent flows give an authoring experience similar to that of Power Automate workflows, native within Copilot Studio.
- Workflows: A new flows format, now in public preview, with a revamped visual designer and improved testing functionality.

You can run flows as standalone automations, or configure a flow to trigger from an agent as a tool, and return results to the same agent. Flows can run prompts, call agents, and include human review steps.

## How does an agent conversation work?

Copilot Studio agents use customized NLU models and AI capabilities to understand what a user types or says, then respond with the best topic. A topic is a portion of a conversational thread between a user and the agent. Learn more in [Create and edit topics](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-create-edit-topics).

For example, you might create an agent for your customers to ask common questions about your business. Your agent reduces support overhead by deflecting support calls. In the agent, you can create a topic about your store's opening hours and name the topic **Store hours**.

When a customer asks a question such as "When do you open?" or "What are your opening hours?", the agent uses natural language understanding (NLU) to understand the *intent* behind the question. The agent matches that intent to the best topic, the **Store hours** topic.

The agent follows the *conversation flow* —which is a group of connected nodes—that you define in the **Store hours** topic. Some nodes can ask questions, while others use conditions (if/else) to determine which store the customer wants. The final output of the topic shows the hours and contact information for that specific store.

However, you can't anticipate all the types of questions your customers ask. To help mitigate this issue, Copilot Studio incorporates powerful AI-powered capabilities that use the latest advancements in NLU models. Once your agent is linked to knowledge sources, it can automatically generate responses. These responses are conversational, plain language, and you don't need to create topics for every eventuality.

You can also choose to let your agent access information outside its knowledge sources.

Copilot Studio can use AI powered by the Azure OpenAI GPT model, also used in Bing, to create topics from a simple description of your needs. Similarly, you can modify and update any topic in your agent by describing the changes you want to make.

## Access Copilot Studio

Access Copilot Studio as a standalone web app at [https://copilotstudio.microsoft.com](https://copilotstudio.microsoft.com/).

Note

After the end of June 2026, it will no longer be possible to use the [Copilot Studio for Teams](https://aka.ms/PVATeamsApp?azure-portal=true) app to create classic chatbots. The app will redirect makers to the Copilot Studio web app instead.

### What can I do with a standalone Copilot Studio subscription?

If you have a standalone Copilot Studio subscription, you can create agents that have generative AI capabilities.

Use cases:

- You're an IT admin who wants to create agents to perform tasks or interact with customers.
- You're familiar with agent services and want to trial or test Copilot Studio.
- You want to explore advanced agent concepts, such as entities and variables, and create complex agents.

Learn more in [Quickstart: Create and deploy an agent](https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-get-started).

### What can I do with the Teams plan?

If you have the [Teams plan](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing-subscriptions#copilot-studio-for-microsoft-teams-plan), available in select Microsoft 365 subscriptions, you can use the Copilot Studio web app to create agents that use classic orchestration and publish them to Microsoft Teams only.

Use cases:

- You're an employee or member of an organization who wants to use agents to answer common employee questions.
- You want to use advanced concepts, such as entities and variables, and have an agent internally available in Teams.
- You want to create and distribute an agent quickly.

Learn more in [Quickstart: Create a classic agent and publish it to Microsoft Teams](https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-get-started-teams).

## Plan your agent

Consider the following points when planning your agent.

### Extend Microsoft 365 Copilot with an agent

Consider extending Microsoft 365 Copilot with an agent if:

- You want to craft your own agent by declaring instructions, tools, and knowledge to customize Microsoft 365 Copilot for specific tasks and domain knowledge.
- You wish to utilize the existing Copilot orchestrator.
- You want a standalone custom version of the Microsoft 365 Copilot chat experience.

Learn more in [Extend Microsoft 365 Copilot with agents](https://learn.microsoft.com/en-us/microsoft-copilot-studio/microsoft-copilot-extend-copilot-extensions).

### Create an agent

Copilot Studio makes it easy to create agents. Just describe the agent you want in plain language. Tell Copilot Studio what specific instructions, triggers, knowledge sources, and tools you want for your agent. Then test your agent before you deploy it. Publish your agent when you're ready across multiple channels.

Consider creating an agent if:

- You want an agent that can:
	- Integrate company data and documents
		- Retrieve real-time data from external APIs
		- Take actions in response to external events
		- Be embedded in company applications
- You require a customized end-to-end solution for your web or mobile app or automation workflow that meets specific business needs and allows for complete control over product branding.
- You want to surface your agent to other agents as their supported agent extension.
- You're a proficient developer looking to create a customized end-to-end solution to cater to your business needs, and want:
	- Full control on product branding
		- Choice of language models and orchestration
	Or, if you're building products like:
	- A customer service chatbot for your e-commerce site
		- A virtual assistant to schedule appointments for your healthcare service
		- Gaming experiences that incorporate generative AI

## Accessibility

The agent authoring canvas is built for accessibility in accordance with [Microsoft accessibility guidelines](https://www.microsoft.com/accessibility/) and supports standard navigational patterns.

## Important information

Important

Microsoft Copilot Studio (1) is not intended or made available as a medical device for the diagnosis of disease or other conditions, or in the cure, mitigation, treatment or prevention of disease, or otherwise to be used as a component of any clinical offering or product, and no license or right is granted to use Microsoft Copilot Studio for such purposes, (2) is not designed or intended to be a substitute for professional medical advice, diagnosis, treatment, or judgment and should not be used as a substitute for, or to replace, professional medical advice, diagnosis, treatment, or judgment, and (3) should not be used for emergencies and does not support emergency calls. Any agent you create using Microsoft Copilot Studio is your own product or service, separate and apart from Microsoft Copilot Studio. You are solely responsible for the design, development, and implementation of your agent (including incorporation of it into any product or service intended for medical or clinical use) and for explicitly providing end users with appropriate warnings and disclaimers pertaining to use of your agent. You are solely responsible for any personal injury or death that may occur as a result of your agent or your use of Microsoft Copilot Studio in connection with your agent, including (without limitation) any such injuries to end users.

## Related content

- [AI-based agent authoring overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/nlu-gpt-overview)
- [Create and delete agents](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-first-bot)
- [Create and edit topics](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-create-edit-topics)
- [Key concepts - Publish and deploy your agent](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels)
- [Analytics overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-overview)
- [Agent flows overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-overview)