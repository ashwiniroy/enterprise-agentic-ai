# Enterprise Agentic AI Platform

## Project Status, Architecture, Deployment, CI/CD, and Integration Roadmap

**Status:** Working backend deployed to Azure with automated GitHub -\>
Azure DevOps -\> ACR -\> Azure Container Apps CI/CD.\
**Next major phase:** Integrate the existing React frontend and the
existing ReviewAnalyticsPlatform .NET API, then expand the platform for
Admin, Support, and Customer personas.

------------------------------------------------------------------------

## 1. Project Vision

The goal is to build an enterprise e-commerce Agentic AI platform that
combines traditional application capabilities with:

-   Azure OpenAI
-   Retrieval-Augmented Generation (RAG)
-   PostgreSQL + pgvector
-   LangChain / LangGraph-style agent orchestration
-   Business tools and APIs
-   Human-in-the-loop workflows
-   Review and sentiment analytics
-   Refund and support automation
-   Role-based experiences for Admin, Support, and Customer users

The platform should not be only a chatbot. AI should be able to retrieve
enterprise knowledge, reason over business context, call approved tools,
assist employees, and perform controlled business actions.

------------------------------------------------------------------------

## 2. Target User Roles

### 2.1 Admin

The Admin experience is focused on business visibility and AI-assisted
analysis.

Planned capabilities include:

-   Overall business dashboard
-   Total returns
-   Total refunds
-   Refund amount and trends
-   Approved / rejected / pending refunds
-   Total support tickets
-   Open / resolved / escalated tickets
-   Average ticket resolution time
-   Product-level return trends
-   Review volume
-   Positive / neutral / negative sentiment
-   Customer satisfaction indicators
-   Products receiving negative feedback
-   Common customer complaints
-   Return/refund reasons
-   AI-assisted business analysis

Example Admin AI questions:

-   Why did refunds increase this month?
-   Which products have the highest negative sentiment?
-   What are customers saying about Product X?
-   Which products generate the most support tickets?
-   What are the main reasons customers return products?
-   Summarize customer satisfaction this month.

Admin AI will eventually combine structured operational data with
unstructured enterprise knowledge.

### 2.2 Support

The Support role acts as an AI-assisted support workbench.

Planned capabilities include:

-   View support tickets
-   View assigned tickets
-   Search customers
-   View order information
-   View customer history
-   View refund requests
-   Approve or reject manual refund requests
-   Escalate cases
-   Ask AI about policies
-   Summarize customer conversations
-   Generate suggested responses
-   Check refund/return eligibility
-   Use AI as a support copilot

Example workflow:

``` text
Customer refund request
        |
        v
Order lookup
        |
        v
Policy retrieval
        |
        v
Eligibility evaluation
        |
        +---------------------+
        |                     |
        v                     v
Auto-approval           Manual review
                              |
                              v
                       Support approval
                              |
                         +----+----+
                         |         |
                         v         v
                      Approve    Reject
```

This provides a Human-in-the-Loop pattern for Agentic AI.

### 2.3 Customer

The Customer experience is focused on self-service.

Planned capabilities include:

-   View products
-   View own orders
-   Write product reviews
-   Ask AI about products
-   Ask AI about return/refund policies
-   Ask whether an order is eligible for return
-   Request a refund through AI
-   Track refund status
-   Create support tickets
-   Chat with an AI customer assistant

Example:

``` text
Customer:
Can I return my iPhone?

AI:
Please provide your order number.

Customer:
ORD-1001

AI:
Order found.
Product: iPhone
Return policy retrieved.
Eligibility checked.

The order is eligible for return.

Would you like to create a refund request?
```

Depending on business rules, a refund can either be automatically
approved or routed to Support for manual approval.

------------------------------------------------------------------------

## 3. High-Level Architecture

``` text
                           React Frontend
                                |
              +-----------------+-----------------+
              |                 |                 |
              v                 v                 v
            Admin             Support           Customer
              |                 |                 |
              +-----------------+-----------------+
                                |
                                v
                         Application APIs
                      FastAPI + existing .NET API
                                |
                +---------------+----------------+
                |               |                |
                v               v                v
             Agents            RAG          Business Tools
                |               |                |
                |               v                |
                |       PostgreSQL + pgvector    |
                |               |                |
                +---------------+----------------+
                                |
                                v
                           Azure OpenAI
                                |
                                v
                     Controlled AI Response/Action
```

The existing .NET ReviewAnalyticsPlatform will be integrated rather than
discarded. FastAPI will remain useful for the AI/agent layer, while the
.NET API can continue providing existing review/business functionality.

------------------------------------------------------------------------

## 4. Backend Work Completed

A FastAPI backend has been created and containerized.

Important working functionality includes:

-   FastAPI application startup
-   `/api/health`
-   `/api/ask`
-   RAG pipeline
-   Azure OpenAI integration
-   PostgreSQL connectivity
-   pgvector
-   LangChain PostgreSQL vector store
-   Source-aware RAG responses
-   Azure-hosted deployment

Example successful local/hosted RAG request:

``` json
{
  "question": "What is the return policy for iPhone?"
}
```

The backend returns an answer together with source metadata such as:

``` json
{
  "answer": "The return policy ...",
  "sources": [
    {
      "file_name": "products.xlsx",
      "sheet": "Products",
      "row": 3
    },
    {
      "file_name": "refund-policy.pdf",
      "page": 0
    }
  ]
}
```

This source metadata will later be displayed in the React UI.

------------------------------------------------------------------------

## 5. RAG Architecture

Current conceptual RAG flow:

``` text
User question
     |
     v
FastAPI /api/ask
     |
     v
Retriever
     |
     v
PGVectorStore
     |
     v
PostgreSQL + pgvector
     |
     v
Relevant document chunks
     |
     v
Azure OpenAI
     |
     v
Answer + source metadata
```

The vector table currently used is:

``` text
enterprise_knowledge
```

The table contains the LangChain-compatible columns:

``` text
langchain_id       UUID
content            TEXT
embedding          VECTOR(1536)
langchain_metadata JSON
```

The PostgreSQL `vector` extension is enabled.

------------------------------------------------------------------------

## 6. Azure PostgreSQL Authentication

The application was moved toward Microsoft Entra / Managed Identity
authentication instead of storing a normal PostgreSQL password in the
application.

The Azure Container App has a System Assigned Managed Identity.

The backend uses `DefaultAzureCredential` and obtains a PostgreSQL token
using:

``` text
https://ossrdbms-aad.database.windows.net/.default
```

SQLAlchemy injects the access token as the database password when a
connection is created.

The important architecture is:

``` text
Azure Container App
        |
        v
System Assigned Managed Identity
        |
        v
DefaultAzureCredential
        |
        v
Entra access token
        |
        v
Azure Database for PostgreSQL
```

The PostgreSQL principal for the Container App was created/configured
and permissions were granted to the application identity.

A key issue found during deployment was that the identity initially had
schema access but did not have `SELECT` permission on
`public.enterprise_knowledge`. After correcting database permissions,
the database-backed RAG functionality worked.

------------------------------------------------------------------------

## 7. Database Connection Implementation

The application currently uses SQLAlchemy with sync and async engines.

Conceptually:

``` python
credential = DefaultAzureCredential()

POSTGRES_SCOPE = (
    "https://ossrdbms-aad.database.windows.net/.default"
)

# SQLAlchemy connection event:
token = credential.get_token(POSTGRES_SCOPE)
cparams["password"] = token.token
```

This supports:

-   synchronous application/database operations
-   asynchronous RAG/PGVector operations

The async engine is used by the LangChain PostgreSQL vector store.

------------------------------------------------------------------------

## 8. Important Problems Solved During Azure Deployment

Several production-style deployment issues were identified and fixed.

### 8.1 Container revision activation failure

An early Azure Container Apps revision entered:

``` text
ActivationFailed
```

The container was terminating with exit code `1`.

### 8.2 CPU architecture mismatch

One image failed with:

``` text
exec /usr/local/bin/python: exec format error
```

This was caused by building an incompatible image architecture on an
ARM-based Mac for the Azure runtime.

The image was rebuilt for the appropriate Linux architecture.

### 8.3 Missing application configuration

Pydantic initially reported missing settings including:

``` text
azure_openai_api_key
postgres_user
```

The required Azure Container Apps environment variables were configured.

### 8.4 Managed Identity PostgreSQL authentication

The application initially failed with:

``` text
EntraConnectionValueError:
Could not retrieve Entra credentials
```

The database authentication implementation and Azure identity
configuration were investigated and corrected.

### 8.5 PostgreSQL firewall

Azure Database for PostgreSQL had public network access enabled, but the
firewall initially only contained the developer machine's IP.

The Azure workload/network access was corrected so the Container App
could communicate with PostgreSQL.

### 8.6 PGVector table mismatch

A later error was:

``` text
ValueError:
Id column, langchain_id, does not exist.
```

The actual `enterprise_knowledge` schema was inspected and validated:

``` text
langchain_id
content
embedding
langchain_metadata
```

The database/table context and permissions were corrected.

### 8.7 Database authorization

The managed identity existed as a PostgreSQL role, but initially:

``` text
schema_usage = true
can_select    = false
```

Appropriate table privileges were granted.

After these fixes, the backend and RAG flow worked successfully.

------------------------------------------------------------------------

## 9. Azure Container Apps Deployment

The backend is deployed to Azure Container Apps.

Current application:

``` text
enterprise-ai-backend
```

Resource group:

``` text
DefaultResourceGroup-EAU
```

Container Apps environment:

``` text
enterprise-ai-env
```

The backend has an Azure Container Apps FQDN and `/api/health` returns a
successful response.

The application listens on:

``` text
0.0.0.0:8000
```

------------------------------------------------------------------------

## 10. Azure Container Registry

Docker images are stored in Azure Container Registry:

``` text
myaicr220412.azurecr.io
```

Image repository:

``` text
enterprise-agentic-ai-backend
```

The ACR resource exists in:

``` text
VisualStudioOnline-083E3900FB28435FBD7B1A8E3090CB5D
```

------------------------------------------------------------------------

## 11. Git and GitHub

The project was initialized as a Git repository:

``` bash
git init
git branch -M main
```

Sensitive configuration is excluded using `.gitignore`.

In particular, `.env` was confirmed to be ignored.

The GitHub repository is:

``` text
ashwiniroy/enterprise-agentic-ai
```

The standard development workflow is now:

``` bash
git add .
git commit -m "description of change"
git push origin main
```

------------------------------------------------------------------------

## 12. Azure DevOps CI/CD

A GitHub-backed Azure DevOps pipeline has been configured.

Current flow:

``` text
Developer
    |
    | git push
    v
GitHub main
    |
    v
Azure DevOps Pipeline
    |
    +--> Python validation / CI
    |
    +--> Docker build
    |
    v
Azure Container Registry
    |
    v
Azure Container Apps deployment
```

The pipeline builds an immutable build-tagged Docker image and deploys
the backend.

### CI/CD authentication

An Azure Resource Manager service connection was configured.

The service principal required appropriate Azure RBAC.

Important permissions added:

-   `AcrPush` for Azure Container Registry
-   `Contributor` for the Container App deployment scope/resource group

An early pipeline failure returned:

``` text
401 unauthorized
```

during the Docker push. The ACR and pipeline were confirmed to be in the
same Azure subscription, and the service principal's RBAC permissions
were corrected.

After this change, the CI/CD pipeline worked successfully.

------------------------------------------------------------------------

## 13. Current Deployment Flow

The working deployment architecture is:

``` text
GitHub
   |
   v
Azure DevOps
   |
   +--> Validate Python
   |
   +--> Build Docker image
   |
   v
Azure Container Registry
myaicr220412.azurecr.io
   |
   v
Azure Container Apps
enterprise-ai-backend
   |
   v
FastAPI
   |
   +--> Azure OpenAI
   |
   +--> Azure PostgreSQL
             |
             v
           pgvector
```

Dev/QA/Prod promotion, advanced deployment approvals, health probes, and
deeper observability are intentionally deferred for now.

------------------------------------------------------------------------

## 14. Existing React Frontend - Integration Plan

A React frontend codebase already exists and will be integrated rather
than rebuilt.

The codebase includes areas/components for:

-   Dashboard
-   Analytics
-   Reviews
-   AI Search
-   Customer reviews
-   AI chat
-   Suggested questions
-   AI response panels
-   Source/review cards
-   API service/client code

The frontend uses React, Material UI, Axios, routing, forms, charting,
and related UI libraries.

There is already an AI Search concept that calls an AI service. The
frontend API route must be aligned with the deployed FastAPI endpoint.

Target:

``` text
POST /api/ask
```

instead of obsolete/local-only endpoint assumptions.

Environment configuration should be used instead of hardcoding
localhost.

Example concept:

``` text
Local:
REACT_APP_AI_API_URL=http://127.0.0.1:8000/api

Azure:
REACT_APP_AI_API_URL=https://<container-app-domain>/api
```

The UI should also preserve and display RAG sources rather than showing
only `result.answer`.

------------------------------------------------------------------------

## 15. Existing ReviewAnalyticsPlatform .NET API - Integration Plan

An existing ReviewAnalyticsPlatform .NET API codebase will be
incorporated into the platform.

The intention is **not** to rewrite all existing .NET functionality in
FastAPI.

The target responsibility split is:

``` text
React
   |
   +------------------------------+
   |                              |
   v                              v
.NET Business API             FastAPI AI API
   |                              |
   |                              +--> RAG
   |                              +--> Agents
   |                              +--> Azure OpenAI
   |                              +--> AI tools
   |
   +--> Reviews
   +--> Business CRUD
   +--> Existing domain logic
   +--> Analytics data
```

As integration progresses, AI tools can call approved .NET API endpoints
instead of directly duplicating business logic.

For example:

``` text
Refund Agent
     |
     v
Order/Refund Tool
     |
     v
ReviewAnalyticsPlatform / Business API
     |
     v
Database/business rules
```

This maintains separation between deterministic business services and
probabilistic AI reasoning.

------------------------------------------------------------------------

## 16. Planned Role-Based Frontend

The frontend should evolve toward:

``` text
src/
|
+-- pages/
|   |
|   +-- admin/
|   |   +-- Dashboard
|   |   +-- RefundAnalytics
|   |   +-- ReviewAnalytics
|   |   +-- TicketAnalytics
|   |   +-- AIInsights
|   |
|   +-- support/
|   |   +-- Dashboard
|   |   +-- Tickets
|   |   +-- RefundApprovals
|   |   +-- CustomerDetails
|   |   +-- SupportCopilot
|   |
|   +-- customer/
|       +-- Home
|       +-- Orders
|       +-- Reviews
|       +-- Refunds
|       +-- Support
|       +-- ChatAI
```

Existing frontend components should be reused where possible.

------------------------------------------------------------------------

## 17. Planned Agent Architecture

The platform should use a small number of focused business tools rather
than creating unnecessary independent agents.

Proposed architecture:

``` text
                         Supervisor / Router
                                |
          +---------------------+----------------------+
          |                     |                      |
          v                     v                      v
       RAG Tool             Order Tool         Review Analytics Tool
          |                     |                      |
          +----------+----------+----------+-----------+
                     |                     |
                     v                     v
             Eligibility Tool         Ticket Tool
                     |
                     v
                Refund Tool
                     |
                     v
           Approval/Escalation Tool
```

The same tools can be reused across roles, but authorization determines
which tools/actions a user may invoke.

------------------------------------------------------------------------

## 18. Planned Refund Workflow

A central Agentic AI use case is intelligent refund processing.

``` text
Customer asks for refund
        |
        v
Identify authenticated customer
        |
        v
Lookup order
        |
        v
Retrieve applicable policy
        |
        v
Evaluate eligibility
        |
        v
Evaluate automation rules
        |
        +----------------------------+
        |                            |
        v                            v
Automatic path                 Manual path
        |                            |
        v                            v
Create refund              Create approval request
        |                            |
        |                            v
        |                     Support review
        |                       /       \
        |                      /         \
        |                 Approve       Reject
        |                      \         /
        +-----------------------\-------/
                                 |
                                 v
                         Notify customer
```

The AI should not arbitrarily approve financial actions. Deterministic
policy/business rules and authorization must control the actual action.

------------------------------------------------------------------------

## 19. Review Analytics and Sentiment Intelligence

The existing Review Analytics functionality can become a major Admin AI
capability.

Planned analytics include:

-   review count
-   average rating
-   sentiment distribution
-   positive review percentage
-   negative review percentage
-   product-level sentiment
-   category-level sentiment
-   trending complaints
-   recurring product issues
-   feature requests
-   customer satisfaction trends
-   correlation between negative reviews and refunds
-   correlation between reviews and support tickets

Example Admin AI query:

``` text
Why are customers unhappy with Product P1002?
```

Possible AI workflow:

``` text
Admin question
      |
      v
Review analytics tool
      |
      +--> structured review metrics
      |
      +--> relevant negative reviews
      |
      +--> product metadata
      |
      +--> related refund/ticket trends
      |
      v
LLM analysis
      |
      v
Evidence-backed business summary
```

------------------------------------------------------------------------

## 20. Authentication and Authorization Roadmap

Role enforcement must happen in the backend, not only in React.

Target security model:

``` text
Authentication
     |
     v
JWT / Microsoft Entra ID
     |
     v
Role / permission claims
     |
     v
API authorization
```

Example permissions:

### Admin

``` text
analytics:read
reviews:read
refunds:read
tickets:read
ai:business-analysis
```

### Support

``` text
tickets:read
tickets:update
orders:read
refunds:review
ai:support
```

### Customer

``` text
own-orders:read
reviews:create
own-refunds:create
own-refunds:read
tickets:create
ai:customer
```

AI tool execution must honor the same authorization model.

------------------------------------------------------------------------

## 21. Recommended Implementation Sequence From Here

### Phase 1 - Frontend integration

1.  Add the existing React frontend into the main repository.
2.  Clean environment configuration.
3.  Connect React to the deployed FastAPI API.
4.  Connect existing ReviewAnalyticsPlatform APIs.
5.  Display RAG answer + sources.
6.  Establish Admin / Support / Customer route layouts.

### Phase 2 - Core business APIs

1.  Review existing .NET API functionality.
2.  Identify reusable endpoints.
3.  Add order APIs if missing.
4.  Add refund APIs if missing.
5.  Add ticket APIs if missing.
6.  Define shared request/response contracts.

### Phase 3 - Agentic workflows

1.  Implement order lookup tool.
2.  Implement RAG/policy tool.
3.  Implement refund eligibility tool.
4.  Implement refund creation tool.
5.  Implement ticket tool.
6.  Implement approval/escalation workflow.
7.  Add LangGraph state and routing.

### Phase 4 - Role-specific AI

1.  Customer AI Assistant
2.  Support Copilot
3.  Admin Business Analyst

### Phase 5 - Review intelligence

1.  Sentiment aggregation
2.  Product-level trends
3.  Complaint/theme extraction
4.  AI summaries
5.  Cross-analysis of reviews, refunds, orders, and tickets

### Phase 6 - Production hardening (later)

-   automated test suite
-   AI evaluations
-   hallucination/grounding evaluation
-   tool-call evaluation
-   guardrails
-   Application Insights / OpenTelemetry
-   structured logging
-   health/readiness probes
-   Key Vault
-   stronger private networking
-   Dev/QA/Prod environments
-   production approvals
-   deployment rollback
-   cost/token monitoring

------------------------------------------------------------------------

## 22. Current Project Status

### Completed

-   FastAPI backend
-   Azure OpenAI integration
-   RAG pipeline
-   PostgreSQL
-   pgvector
-   enterprise knowledge vector table
-   local RAG testing
-   Azure PostgreSQL connectivity
-   Entra/Managed Identity database authentication
-   Docker containerization
-   Azure Container Registry
-   Azure Container Apps deployment
-   Git repository
-   GitHub repository
-   Azure DevOps pipeline
-   CI Docker build
-   ACR image push
-   CD deployment to Container Apps
-   Service connection and Azure RBAC configuration
-   Working end-to-end CI/CD

### Existing assets to integrate

-   React frontend
-   ReviewAnalyticsPlatform .NET API
-   Existing review functionality
-   Existing dashboard/analytics UI
-   Existing AI Search UI components

### Next focus

``` text
Existing React Frontend
        +
Existing ReviewAnalyticsPlatform .NET API
        +
Current FastAPI Agentic AI Backend
        |
        v
Unified Enterprise Agentic AI Platform
```

------------------------------------------------------------------------

## 23. Target End State

``` text
                              USERS
                                |
             +------------------+------------------+
             |                  |                  |
             v                  v                  v
           ADMIN             SUPPORT            CUSTOMER
             |                  |                  |
             +------------------+------------------+
                                |
                                v
                         React Application
                                |
                   Authentication / RBAC
                                |
               +----------------+----------------+
               |                                 |
               v                                 v
     ReviewAnalyticsPlatform                 FastAPI
          .NET APIs                         AI Gateway
               |                                 |
               |                         Supervisor/Graph
               |                                 |
               |                +----------------+----------------+
               |                |                |                |
               |                v                v                v
               |              RAG Tool       Order Tool      Refund Tool
               |                |                |                |
               |                +----------------+----------------+
               |                                 |
               +----------------+----------------+
                                |
                                v
                     Enterprise Data Layer
                       PostgreSQL / pgvector
                                |
               +----------------+----------------+
               |                                 |
               v                                 v
        Structured Business Data        Enterprise Knowledge
               |                                 |
               +----------------+----------------+
                                |
                                v
                           Azure OpenAI
                                |
                                v
                    Answers + Decisions + Actions
```

The final platform should demonstrate full-stack engineering, cloud
deployment, RAG, agent orchestration, enterprise API integration,
role-based security, human-in-the-loop automation, analytics,
observability/evaluation, and controlled AI-driven business actions.

------------------------------------------------------------------------

## 24. Engineering Principle

The platform should follow this rule:

> **Use AI for understanding, retrieval, reasoning, summarization, and
> orchestration. Use deterministic application code and authorized APIs
> for business rules and irreversible actions.**

Examples:

``` text
AI can:
- understand "refund my iPhone"
- retrieve the applicable policy
- summarize a support ticket
- explain why customers are unhappy
- decide which approved tool should be invoked

Business services should:
- verify authenticated ownership
- calculate exact refund amounts
- enforce refund limits
- update order/refund state
- approve financial transactions according to policy
- write authoritative business records
```

This separation will make the Agentic AI platform safer, easier to test,
and much closer to a real enterprise architecture.
