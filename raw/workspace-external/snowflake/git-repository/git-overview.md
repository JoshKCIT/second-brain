---
source_url: https://docs.snowflake.com/en/developer-guide/git/git-overview
vendor: snowflake
topic: git-repository
fetched_at: 2026-06-10T06:43:23Z
revalidate_after: 2026-07-10T06:43:23Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:snowflake
authority: standard
ingest_mode: defuddle
---

You can integrate your remote Git repository with Snowflake so that files from the remote repository are synchronized to a Git repository clone in Snowflake. The clone includes all branches, tags, and commits from the remote repository.

## Supported platforms

You can integrate Git repositories that use the following platforms. This includes repositories based on these platforms but available at custom URLs. For example, a repository based on GitHub does not need to be at github.com.

- GitHub
- GitLab
- BitBucket
- Azure DevOps
- AWS CodeCommit

## How Snowflake works with a remote Git repository

With a remote Git repository integrated with your Snowflake account, you synchronize files from the remote repository to a Git repository clone in Snowflake. To access a file in Snowflake, you refer to it in the Git repository clone. For more information about using repository files, see [Use a Git repository file as a stored procedure handler](https://docs.snowflake.com/developer-guide/git/git-examples#label-integrating-git-repository-using-procedure).

![Diagram showing Git repository exchanging files with development tools and Snowflake.](https://docs.snowflake.com/static/images/git-architecture.png)

Diagram showing Git repository exchanging files with development tools and Snowflake.

After you integrate your remote repository with Snowflake, you can continue using your development tools and local repository as before. Through the Git repository clone, Snowflake becomes another client of your repository separate from your local repository.

With a Git repository clone in Snowflake, you can do the following:

- Fetch the latest version of branches, tags, and commits from the remote repository.
- Browse folders, search for files, and select branches or tags.
- Copy file paths for referencing in Snowflake code (such as handler code for functions, tasks, or procedures).
- [Execute immediate from](https://docs.snowflake.com/sql-reference/sql/execute-immediate-from) `.sql` files.
- Commit and push changes to the remote repository from [Workspaces](https://docs.snowflake.com/user-guide/ui-snowsight/workspaces-git#label-integrate-a-git-repository), [Streamlit apps](https://docs.snowflake.com/developer-guide/streamlit/features/git-integration), and [Snowflake notebooks](https://docs.snowflake.com/user-guide/ui-snowsight/notebooks-snowgit).
- Import files from the repository clone into code you run in Snowflake, such as procedures and UDFs.