---
source_url: https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html
vendor: aws
topic: comprehend-overview
fetched_at: 2026-06-10T06:24:07Z
revalidate_after: 2026-08-09T06:24:07Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:aws
authority: standard
ingest_mode: defuddle
---

[View a markdown version of this page](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.md)

What is Amazon Comprehend? - Amazon Comprehend

Amazon Comprehend uses natural language processing (NLP) to extract insights about the content of documents. It develops insights by recognizing the entities, key phrases, language, sentiments, and other common elements in a document. Use Amazon Comprehend to create new products based on understanding the structure of documents. For example, using Amazon Comprehend you can search social networking feeds for mentions of products or scan an entire document repository for key phrases.

You can access Amazon Comprehend document analysis capabilities using the Amazon Comprehend console or using the Amazon Comprehend APIs. You can run real-time analysis for small workloads or you can start asynchronous analysis jobs for large document sets. You can use the pre-trained models that Amazon Comprehend provides, or you can train your own custom models for classification and entity recognition.

Amazon Comprehend may store your content to continuously improve the quality of its pre-trained models. See the [Amazon Comprehend FAQ](https://aws.amazon.com/comprehend/faqs/) to learn more.

All of the Amazon Comprehend features accept UTF-8 text documents as the input. In addition, custom classification and custom entity recognition accept image files, PDF files, and Word files as input.

Amazon Comprehend can examine and analyze documents in a variety of languages, depending on the specific feature. For more information, see [Languages supported in Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html). Amazon Comprehend's [Dominant language](https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html) capability can examine documents and determine the dominant language for a far wider selection of languages.

## Amazon Comprehend insights

Amazon Comprehend uses a pre-trained model to examine and analyze a document or set of documents to gather insights about it. This model is continuously trained on a large body of text so that there is no need for you to provide training data.

Amazon Comprehend analyzes the following types of insights:

- **Entities** – References to the names of people, places, items, and locations contained in a document.
- **Key phrases** – Phrases that appear in a document. For example, a document about a basketball game might return the names of the teams, the name of the venue, and the final score.
- **Personally Identifiable Information (PII)** – Personal data that can identify an individual, such as an address, bank account number, or phone number.
- **Language** – The dominant language of a document.
- **Sentiment** – The dominant sentiment of a document, which can be positive, neutral, negative, or mixed.
- **Targeted sentiment** – The sentiments associated with specific entities in a document. The sentiment for each entity occurrence can be positive, negative, neutral or mixed.
- **Syntax** – The parts of speech for each word in the document.

For more information, see [Insights](https://docs.aws.amazon.com/comprehend/latest/dg/concepts-insights.html).

## Amazon Comprehend Custom

You can customize Amazon Comprehend for your specific requirements without the skillset required to build machine learning-based NLP solutions. Using automatic machine learning, or AutoML, Amazon Comprehend Custom builds customized NLP models on your behalf, using data you already have.

**Custom classification** – Create custom classification models (classifiers) to organize your documents into your own categories.

**Custom entity recognition** – Create custom entity recognition models (recognizers) that can analyze text for your specific terms and noun-based phrases.

For more information, see [Amazon Comprehend Custom](https://docs.aws.amazon.com/comprehend/latest/dg/concepts-custom.html).

## Flywheels

Use flywheels to simplify the process of training and managing custom model versions over time. A flywheel helps to orchestrate the tasks associated with training and evaluating new versions of a model. Flywheels support plain-text custom models for custom classification and custom entity recognition. For more information, see [Flywheels](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels.html).

## Document clustering (topic modeling)

You can also use Amazon Comprehend to examine a corpus of documents to organize them based on similar keywords within them. Document clustering (topic modeling) is useful to organize a large corpus of documents into topics or clusters that are similar based on word frequency. For more information, see [Topic modeling](https://docs.aws.amazon.com/comprehend/latest/dg/topic-modeling.html).

## Examples

The following examples show how you might use the Amazon Comprehend operations in your applications.

###### Example 1: Find documents about a subject

Find the documents about a particular subject using Amazon Comprehend topic modeling. Scan a set of documents to determine the topics discussed, and to find the documents associated with each topic. You can specify the number of topics that Amazon Comprehend should return from the document set.

###### Example 2: Find out how customers feel about your products

If your company publishes a catalog, let Amazon Comprehend tell you what customers think of your products. Send each customer comment to the `DetectSentiment` operation and it will tell you whether customers feel positive, negative, neutral, or mixed about a product.

###### Example 3: Discover what matters to your customers

Use Amazon Comprehend topic modeling to discover the topics that your customers are talking about on your forums and message boards, then use entity detection to determine the people, places, and things that they associate with the topic. Use sentiment analysis to determine how your customers feel about a topic.

## Benefits

Benefits of using Amazon Comprehend include:

- **Integrate powerful natural language processing into your apps** – Amazon Comprehend removes the complexity of building text analysis capabilities into your applications by making powerful and accurate natural language processing available with a simple API. You don't need textual analysis expertise to take advantage of the insights that Amazon Comprehend produces.
- **Deep learning based natural language processing** – Amazon Comprehend uses deep learning technology to accurately analyze text. Our models are constantly trained with new data across multiple domains to improve accuracy.
- **Scalable natural language processing** – Amazon Comprehend enables you to analyze millions of documents so that you can discover the insights that they contain.
- **Integrated with other AWS services** – Amazon Comprehend is designed to work seamlessly with other AWS services like Amazon S3, AWS KMS, and AWS Lambda. Store your documents in Amazon S3, or analyze real-time data with Firehose. Support for AWS Identity and Access Management (IAM) makes it easy to securely control access to Amazon Comprehend operations. Using IAM, you can create and manage users and groups to grant the appropriate access to your developers and end users.
- **Encryption of output results and volume data** – Amazon S3 already enables you to encrypt your input documents, and Amazon Comprehend extends this even farther. By using your own KMS key, you can encrypt the output results of your job and the data on the storage volume attached to the compute instance that processes the analysis job. The result is significantly enhanced security.
- **Low cost** – With Amazon Comprehend, there are no minimum fees or upfront commitments. You pay for the documents that you analyze and custom models that you train.

## Amazon Comprehend pricing

With Amazon Comprehend, you pay only for the resources that you use. If you are a new AWS customer, you can get started with Amazon Comprehend for free. For more information, see [AWS free usage tier](https://aws.amazon.com/free/).

There is a usage charge for running real-time or asynchronous analysis jobs. You pay to train custom models, and you pay for custom model management. For real-time requests using custom models, you pay for the endpoint from the time that you start your endpoint until you delete the endpoint. There is no additional charge for using flywheels. However, when you run a flywheel iteration, you incur the standard charges for training a new model version and storing the model data.

For the rates and additional detailed information, see [Amazon Comprehend Pricing](https://aws.amazon.com/comprehend/pricing).

## Are you a first-time user of Amazon Comprehend?

If you are a first-time user of Amazon Comprehend, we recommend that you read the following sections in order:

1. **[How it works](https://docs.aws.amazon.com/comprehend/latest/dg/how-it-works.html)** – This section introduces Amazon Comprehend concepts.
2. **[Setting up](https://docs.aws.amazon.com/comprehend/latest/dg/setting-up.html)** – In this section, you create an account and set up the AWS CLI.
3. **[Getting started with Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/getting-started.html)** – In this section, you run a Amazon Comprehend analysis job.
4. **[Tutorial: Analyzing insights from customer reviews with Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/tutorial-reviews.html)** – In this section, you perform sentiment and entities analysis and visualize the results.
5. **[Amazon Comprehend API Reference](https://docs.aws.amazon.com/comprehend/latest/APIReference/welcome.html)** – Reference documentation for Amazon Comprehend operations.

AWS provides the following resources for learning about the Amazon Comprehend service:

- The [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/) includes useful articles about Amazon Comprehend.
- [Amazon Comprehend Resources](https://aws.amazon.com/comprehend/resources/) provides useful videos and tutorials about Amazon Comprehend.