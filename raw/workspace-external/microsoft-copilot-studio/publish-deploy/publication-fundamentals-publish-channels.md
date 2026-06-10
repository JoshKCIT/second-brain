---
source_url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels
vendor: microsoft-copilot-studio
topic: publish-deploy
fetched_at: 2026-06-10T07:02:51Z
revalidate_after: 2026-09-08T07:02:51Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:microsoft-copilot-studio
authority: standard
ingest_mode: defuddle
---

## Key concepts - Publish and deploy your agent

By using Copilot Studio, you can publish agents that engage with your customers on multiple platforms or channels. For example, live websites, mobile apps, Microsoft 365 Copilot, and messaging platforms like Teams and Facebook.

Each time you update your agent, you can publish it again from within Copilot Studio. Publishing your agent applies to all the channels associated with your agent.

You need to publish your agent before your customers can engage with it. You can publish your agent on multiple platforms, or *channels*.

After you publish an agent to at least one channel, you can connect it to more channels. Remember to publish your agent again after you make any changes to it.

When you publish an agent, this agent updates on all connected channels. If you make changes to your agent but don't publish after doing so, your customers won't be engaging with the latest content.

Agents have the **Authenticate with Microsoft** option turned on by default. With this option, agents automatically use Microsoft Entra ID authentication for Teams, Power Apps, and Microsoft 365 Copilot without requiring any manual setup.

If you want to allow anyone to chat with an agent, select **No authentication**.

Caution

Selecting the **No authentication** option allows anyone who has the link to chat and interact with your bot or agent.

We recommend you apply authentication, especially if you are using your bot or agent within your organization or for specific users, along with [other security and governance controls](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance).

If you want to use other channels and still have authentication for your agent, select **Authenticate manually**.

Important

If you select **No authentication**, your agent can't use [tools](https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-tools-custom-agent) with [user credentials](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configuration-end-user-authentication).

## Publish the latest content

1. With your agent open for editing, select **Publish**.
2. Select **Publish**, and then confirm. Publishing can take a few minutes.

Tip

To prevent disrupting users who are having an existing conversation with the agent, the latest published content only becomes available after a new session starts. In most channels, a session ends after 30 minutes of inactivity.

In channels that have persistent conversations, such as Microsoft Teams and Omnichannel for Customer Service, you might want to try out the latest published content right away. To do so, enter `start over` in the current session. This command resets the conversation and starts a new session with the latest content you published. Otherwise, it might take one hour after you publish an update for the agent for its latest version to take effect. After this delay, users get the new version the next time they send a message to your agent.

## Test your agent

Test your agent after you publish it. You can [make the agent available to users in Teams and Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams) by using the installation link or from various places in the Microsoft Teams app store.

Start by publishing your agent only for yourself, and test the published version before releasing it to a wider audience. You can install the agent for your own use in Microsoft Teams by selecting **Open the agent in Teams**. You can share your agent later, with members of your team or other stakeholders, by selecting **Make the agent available to others** on the **Publish** page.

Important

Avoid making your agent widely available in Teams or Microsoft 365 Copilot before it's fully configured and tested, and you verified that it's available from the applicable agent stores (if any).

If you selected **No authentication** or **Authenticate manually**, select the **Demo website** link to open a prebuilt website in a new browser tab, where you and your teammates can interact with the agent. The demo website is also useful to gather feedback from stakeholders before you roll your agent out to customers. Learn how to [configure the demo website and add the agent to your live website](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-connect-bot-to-web-channels).

Tip

**What's the difference between the test chat and the demo website?**

- Use the test chat (the **Test agent** panel) while you're building your agent to make sure conversation flows as you expect and to spot errors.
- Only share the demo website URL with members of your team and other stakeholders to try out the agent. The demo website isn't intended for production use. You shouldn't share this URL with customers.

## Configure channels

After you publish your agent at least once, add channels so your customers can reach it.

To configure channels for your agent:

1. On the top menu bar, select **Channels**.
2. Select the channel you want from the list of available channels.
	Each channel has different connection steps. Learn more:
	- [Teams and Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams)
		- [SharePoint](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-add-bot-to-sharepoint)
		- [WhatsApp](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-add-bot-to-whatsapp)
		- [Demo Website](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-connect-bot-to-web-channels)
		- [Custom Website](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-connect-bot-to-web-channels#add-your-agent-to-your-website)
		- [Mobile App](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-connect-bot-to-custom-application)
		- [Facebook](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-add-bot-to-facebook)
		- [Azure Bot Service channels](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-connect-bot-to-azure-bot-service-channels), including:
		- Cortana
				- Slack
				- Telegram
				- Twilio
				- Line
				- Kik
				- GroupMe
				- Direct Line Speech
				- Email

## Channel experience reference table

Different channels offer different user experiences. The following table shows a high-level overview of the experiences for each channel. Consider the channel experiences when you optimize your agent content for specific channels.

| Experience | Website | Teams and Microsoft 365 Copilot | Facebook | Omnichannel for Customer Service |
| --- | --- | --- | --- | --- |
| [Customer satisfaction survey](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-create-edit-topics) | Adaptive card | Text-only | Text-only | Text-only |
| [Multiple-choice options](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-create-edit-topics) | Supported | [Supported up to six (as hero card)](https://learn.microsoft.com/en-us/microsoftteams/platform/concepts/cards/cards-reference#hero-card) | [Supported up to 13](https://developers.facebook.com/docs/messenger-platform/send-messages/quick-replies/) | [Partially Supported](https://learn.microsoft.com/en-us/dynamics365/customer-service/asynchronous-channels#suggested-actions-support) |
| [Markdown](https://daringfireball.net/projects/markdown/) | Supported | [Partially Supported](https://learn.microsoft.com/en-us/microsoftteams/platform/bots/how-to/format-your-bot-messages#text-only-messages) | [Partially supported](https://www.facebook.com/help/147348452522644?helpref=related) | [Partially Supported](https://learn.microsoft.com/en-us/dynamics365/customer-service/asynchronous-channels#preview-support-for-formatted-messages) |
| [Welcome message](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-create-edit-topics) | Supported | Supported | Not supported | Supported for [Chat](https://learn.microsoft.com/en-us/dynamics365/customer-service/set-up-chat-widget). Not supported for other channels. |
| [Did-You-Mean](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-system-topics#multiple-topics-matched) | Supported | Supported | Supported | Supported for [Microsoft Teams](https://learn.microsoft.com/en-us/dynamics365/customer-service/configure-microsoft-teams), [Chat](https://learn.microsoft.com/en-us/dynamics365/customer-service/set-up-chat-widget), Facebook, and text-only channels (short message service (SMS) via [TeleSign](https://learn.microsoft.com/en-us/dynamics365/customer-service/configure-sms-channel) and [Twilio](https://learn.microsoft.com/en-us/dynamics365/customer-service/configure-sms-channel-twilio), [WhatsApp](https://learn.microsoft.com/en-us/dynamics365/customer-service/configure-whatsapp-channel), [WeChat](https://learn.microsoft.com/en-us/dynamics365/customer-service/configure-wechat-channel), and [Twitter](https://learn.microsoft.com/en-us/dynamics365/customer-service/configure-twitter-channel)).   Suggested actions are presented as a text-only list; users must retype an option to respond. |

## Troubleshoot publishing errors

If you run into problems when publishing your agent, use the following troubleshooting steps to resolve common publishing errors:

1. **Verify all configurations are correct.** Make sure that the agent settings, authentication options, and channel configurations are set up properly before publishing.
2. **Check for any missing dependencies.** Ensure that all required components, such as topics, flows, connectors, and data sources, are available and properly configured.
3. **Review error logs for specific error codes and messages.** Go to the **Publish** page and check the publish status for any error details. Use the error codes and messages to identify and address the root cause.

## Known limitations

- The customer satisfaction survey in Microsoft Teams is a text-only version instead of an adaptive card.
- Microsoft Teams can render up to six suggested actions in one question node.
- A user can't send or upload attachments to the chat. If they try to send an attachment, the agent replies: *Looks like you tried to send an attachment. Currently, I can only process text. Please try sending your message again without the attachment.*
	- This limitation applies to all channels, even if the channel or user-facing experience supports attachments. For example, this limitation applies to the Direct Line API and Microsoft Teams.
		- Attachments can be supported if the message is sent to a skill, where the skill bot supports the processing of attachments. Learn more in [Use Microsoft Bot Framework skills in Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-use-skills).

## Next steps

- [Web app](#tabpanel_1_web)
- [Teams](#tabpanel_1_teams)

| Article | Description |
| --- | --- |
| [Publish an agent to a live or demo website](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-connect-bot-to-web-channels) | Publish your agent on your live website, or use a demo website to share internally. |
| [Connect and configure an agent for Teams and Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams) | Use Teams and Microsoft 365 Copilot to distribute your agent. |
| [Publish an agent to Facebook](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-add-bot-to-facebook) | Add your agent to Facebook Messenger. |
| [Publish an agent to mobile or custom apps](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-connect-bot-to-custom-application) | Add your agent to mobile or custom native apps (developer coding required). |
| [Publish an agent to Azure Bot Service channels](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-connect-bot-to-azure-bot-service-channels) | Add your agent to Azure Bot Service channels (developer coding required). |