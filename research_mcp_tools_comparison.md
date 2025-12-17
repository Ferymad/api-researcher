# Research MCP Servers Comparison for Deep API Documentation Research

## Executive Summary

This document compares research-focused MCP servers that can enhance deep API documentation research capabilities. The analysis covers 8 major tools across search, scraping, and crawling functionality.

**Key Finding**: For deep API documentation research, a combination of **Jina AI** (free, rate-limited), **Brave Search** (2,000 free queries/month), and **Firecrawl** (500 free pages) provides the best free-tier coverage. For production use, **Tavily** or **Exa** offer superior quality at reasonable costs.

---

## 1. Tavily MCP Server

### Package & Installation
- **Package**: `@mcptools/mcp-tavily`
- **Remote Server**: `https://mcp.tavily.com/mcp/` (recommended)
- **Installation**: `npx -y @mcptools/mcp-tavily`

### Purpose
AI-powered search API specifically designed for LLMs, optimized to reduce hallucinations and deliver fast, relevant results for AI agents.

### Key Features
1. **tavily-search**: Real-time web search with configurable depth
   - Search depth: "basic" or "advanced"
   - Include images, max results
   - Topic filtering: "general", "news", "finance"
   - Date range filtering

2. **tavily-extract**: Intelligent data extraction from web pages for structured information retrieval

3. **tavily-map**: Creates structured website architecture maps for navigation visualization

4. **tavily-crawl**: Systematic web crawler for comprehensive site discovery

### Pricing
- **Free Tier**: Limited (exact limits not publicly disclosed in research)
- **Paid Plans**: Pay-as-you-go starting at approximately $8 CPM (cost per thousand searches)
- Comparison: More expensive than Brave ($3 CPM) but cheaper than many alternatives

### API Key Requirements
- **Required**: Yes
- **How to obtain**: Sign up at https://tavily.com
- **Setup**: Set `TAVILY_API_KEY` environment variable

### Recommendation for Our Use Case
**YES - Highly Recommended**

**Strengths**:
- Purpose-built for AI agents
- Multiple complementary tools (search, extract, map, crawl)
- Production-ready with remote server option
- Reduces LLM hallucinations with high-quality results

**Considerations**:
- Higher cost than Brave Search
- Free tier limits unclear - may require paid plan for heavy research

**Best For**: Production agencies requiring comprehensive web research with extraction, mapping, and crawling capabilities.

---

## 2. Firecrawl MCP Server

### Package & Installation
- **Official Package**: `firecrawl-mcp`
- **Alternative**: `@modelcontextprotocol/mcp-server-firecrawl`
- **Installation**: `npx -y firecrawl-mcp`

### Purpose
Web scraping and crawling tool optimized for modern JavaScript-heavy websites, converting web content to clean LLM-ready markdown.

### Key Features
1. **Web Scraping**: Extract content from individual URLs with JavaScript rendering
2. **Crawling**: Navigate and scrape multiple pages from websites
3. **Batch Processing**: Efficient parallel processing with rate limiting
4. **Markdown Conversion**: Clean, LLM-friendly markdown output
5. **Search Capabilities**: 2 credits per 10 results
6. **Automatic Retries**: Exponential backoff for reliability
7. **Self-Hosted Support**: Can use cloud or self-hosted instances

### Pricing
- **Free Tier**: 500 credits (500 pages)
- **Hobby**: $16/month for 3,000 credits
- **Standard**: $83/month for 100,000 credits
- **Growth**: $333/month for 500,000 credits
- **Extract Plans**: Starting at $89/month

**Credit System**:
- 1 credit = 1 page scraped (standard conditions)
- 2 credits = 10 search results
- Transparent pricing with no hidden fees

### API Key Requirements
- **Required**: Yes
- **How to obtain**:
  1. Sign up at https://www.firecrawl.dev
  2. Get API key from https://www.firecrawl.dev/app/api-keys
- **Setup**: Set `FIRECRAWL_API_KEY` environment variable

### Recommendation for Our Use Case
**YES - Highly Recommended**

**Strengths**:
- Excellent free tier (500 pages for testing)
- JavaScript rendering for modern sites
- Clean markdown output ideal for LLM consumption
- Transparent credit-based pricing
- Self-hosted option for privacy/cost control

**Considerations**:
- Credits consumed per page can add up quickly
- May need paid plan for extensive documentation crawling

**Best For**: Agencies needing to extract clean documentation from modern websites, especially those with JavaScript-heavy content.

---

## 3. Perplexity MCP Server

### Package & Installation
- **Official Package**: `@perplexity-ai/mcp-server`
- **Community**: `perplexity-mcp` (by jsonallen, cyanheads)
- **Installation**: `npx -y @perplexity-ai/mcp-server`

### Purpose
AI-powered search and reasoning platform providing conversational AI, deep research, and advanced problem-solving capabilities.

### Key Features
1. **perplexity_search**: Direct web search using Perplexity Search API
   - Returns ranked results with titles, URLs, snippets, metadata
   - Best for current information and facts

2. **perplexity_ask**: General conversational AI with real-time web search
   - Model: sonar-pro
   - Best for quick questions and everyday searches

3. **perplexity_research**: Deep, comprehensive research
   - Model: sonar-deep-research
   - Provides thorough analysis with citations
   - Best for complex topics requiring detailed investigation

4. **perplexity_reason**: Advanced reasoning and problem-solving
   - Model: sonar-reasoning-pro
   - Best for logical problems and decision-making

**Optional**: `strip_thinking` parameter to remove reasoning tags and conserve tokens

### Pricing
- **Pricing Model**: Token-based (like OpenAI)
- **Free Tier**: Details not clearly disclosed in public documentation
- **Paid Plans**: Pay-per-use based on tokens consumed
- Cost varies by model (sonar-pro vs sonar-deep-research vs sonar-reasoning-pro)

### API Key Requirements
- **Required**: Yes
- **How to obtain**:
  1. Visit Perplexity API Portal
  2. Sign up and create API key
- **Setup**: Set `PERPLEXITY_API_KEY` environment variable
- **Optional**: `PERPLEXITY_TIMEOUT_MS` (default: 300000ms/5min)
- **Proxy Support**: Set `PERPLEXITY_PROXY`, `HTTPS_PROXY`, or `HTTP_PROXY`

### Recommendation for Our Use Case
**MAYBE - Specialized Use**

**Strengths**:
- Excellent for deep research with citations
- Multiple models for different use cases
- Strong reasoning capabilities
- Well-maintained official MCP server

**Considerations**:
- Token-based pricing can be expensive for heavy use
- More suited for question-answering than bulk API discovery
- Overlaps with OpenAI functionality already in Agency Swarm

**Best For**: Agencies requiring expert-level research with citations and reasoning, particularly for complex decision-making tasks. Less optimal for bulk API documentation extraction.

---

## 4. Brave Search MCP Server

### Package & Installation
- **Official Package**: `@modelcontextprotocol/server-brave-search`
- **Installation**: `npx -y @modelcontextprotocol/server-brave-search`

### Purpose
Privacy-focused web and local search API integrating Brave's independent search index.

### Key Features
1. **Web Search**: General queries, news, articles
   - Pagination support
   - Freshness controls
   - Safety level filtering
   - Result type filtering

2. **Local Search**: Find businesses and services
   - Detailed descriptions
   - Automatic fallback to web search if no local results

3. **Smart Fallbacks**: Automatic web search fallback for local queries with no results

### Pricing
- **Free Tier**: 2,000 queries/month at 1 query/second
- **Paid Plans**: Starting at $3 CPM (cost per thousand queries)
  - 20 queries/second
  - Up to 20 million queries/month
  - Add-ons: Autosuggest & spellcheck at $5 per 10,000 requests

**Free Tier Details**:
- No credit card required for free tier
- Card only used for identity verification (not charged)
- Includes web search, Goggles, news cluster, videos cluster

### API Key Requirements
- **Required**: Yes
- **How to obtain**:
  1. Sign up at https://brave.com/search/api/
  2. Create free account (up to 2,000 queries/month)
  3. Get API key from dashboard
- **Setup**: Set `BRAVE_API_KEY` environment variable

### Recommendation for Our Use Case
**YES - Highly Recommended for Free Tier**

**Strengths**:
- Generous free tier (2,000 queries/month)
- No credit card required
- Lowest cost per thousand at $3 CPM
- Privacy-focused (no tracking)
- Official MCP implementation
- MIT license

**Considerations**:
- Fewer features than Tavily (no extract, map, crawl)
- Basic search functionality only

**Best For**: Budget-conscious agencies or those requiring a reliable, privacy-focused search API with a substantial free tier. Ideal as a primary search tool to complement specialized scrapers.

---

## 5. Exa MCP Server

### Package & Installation
- **Official Package**: `exa-mcp-server`
- **Remote Server**: `https://mcp.exa.ai/mcp`
- **Installation**: `npx -y exa-mcp-server`

### Purpose
Meaning-based semantic web search API powered by embeddings, designed to find data that traditional keyword search misses.

### Key Features
1. **web_search_exa**: Real-time semantic web search
   - Optimized results with content extraction
   - Meaning-based, not just keyword matching

2. **deep_search_exa**: Deep web search with smart query expansion
   - High-quality summaries for each result
   - Comprehensive analysis

3. **get_code_context_exa**: Search code, documentation, and examples
   - Open source libraries and GitHub repositories
   - API usage patterns and best practices
   - Up-to-date code documentation

4. **company_research**: Comprehensive company information
   - Crawls company websites
   - Detailed business intelligence

5. **research_paper_search**: Academic papers and research content

6. **competitor_finder**: Identify similar companies and competitors

7. **linkedin_search**: Search LinkedIn for companies and people

8. **crawling**: Extract content from specific URLs

### Pricing
- **Free Tier**: $10 in free credits for new users (also reported as $20 in some sources)
- **Pay-per-use**: $5 per 1,000 searches
- **Websets**: 1,000 free credits
- **Monthly Plans**: Starting at $49/month (reported in some sources)

**Note**: Pricing varies by endpoint and search method (Neural vs. others)

### API Key Requirements
- **Required**: Yes
- **How to obtain**:
  1. Sign up at https://exa.ai
  2. Get API key from dashboard
- **Setup**: Set `EXA_API_KEY` environment variable

### Recommendation for Our Use Case
**YES - Highly Recommended**

**Strengths**:
- Semantic search finds relevant content better than keyword search
- **get_code_context_exa** is perfect for API documentation discovery
- Multiple specialized tools for different research needs
- Academic paper search for technical documentation
- Free credits sufficient for testing
- Meaning-based search reduces irrelevant results

**Considerations**:
- More expensive than Brave at $5/1000 vs $3/1000
- Free tier limited to $10-20 in credits
- Complex pricing structure

**Best For**: Agencies requiring high-quality, semantic search for API documentation, code examples, and technical research. The code context tool is particularly valuable for discovering implementation patterns.

---

## 6. Olostep MCP Server

### Package & Installation
- **Package**: `olostep-mcp`
- **Installation**: `npx -y olostep-mcp`

### Purpose
Fast, cost-effective web scraping with clean markdown conversion and Google search integration.

### Key Features
1. **get_webpage_content**: Extract webpage content in clean markdown
   - JavaScript rendering support
   - Country-specific routing (US, CA, GB, etc.)
   - Configurable wait times before scraping

2. **Google Search**: Structured search results
   - Country-specific request routing
   - JavaScript rendering support

3. **Website Mapping**: URLs sorted by relevance to search query

### Pricing
- **Free Tier**: Not clearly disclosed in public documentation
- **Paid Plans**: Described as "cost-effective" but specific pricing not found

### API Key Requirements
- **Required**: Yes
- **How to obtain**: Sign up at https://olostep.com
- **Setup**: Set `OLOSTEP_API_KEY` environment variable

### Recommendation for Our Use Case
**MAYBE - Depends on Pricing**

**Strengths**:
- Clean markdown conversion
- Google search integration
- JavaScript rendering
- Country-specific routing
- Fast performance

**Considerations**:
- Pricing details unclear (transparency issue)
- Limited documentation available
- Smaller community compared to Firecrawl
- Overlaps with Firecrawl functionality

**Best For**: Agencies already using Google search and needing fast markdown conversion. However, Firecrawl offers similar functionality with clearer pricing.

---

## 7. Search1API MCP Server

### Package & Installation
- **Package**: `search1api-mcp`
- **Installation**: `npx -y search1api-mcp`

### Purpose
Unified API for search, crawling, and sitemap extraction across multiple search services.

### Key Features
1. **Search Tool**: Multi-service web search
   - Services: Google, Bing, DuckDuckGo, Yahoo, X (Twitter), Reddit, GitHub, YouTube, arXiv, WeChat, Bilibili, IMDb, Wikipedia
   - Customizable parameters (time range, site filtering)

2. **Crawl Tool**: Extract full content from URLs
   - `crawl_results` parameter for batch crawling
   - Site include/exclude filters

3. **Sitemap Tool**: Retrieve all related links from a URL

4. **News Tool**: News article search

5. **Reasoning Tool**: Leverage DeepSeek R1 model for complex problem-solving

6. **Trending**: Access trending topics from GitHub and Hacker News

### Pricing
- **Plans**: 25,000 credits per month (reported)
- **Free Tier**: Not clearly disclosed
- **Paid Plans**: Specific pricing not found in research

**Note**: Pricing transparency is limited

### API Key Requirements
- **Required**: Yes
- **How to obtain**: Sign up at https://www.search1api.com
- **Setup**: Set `SEARCH1API_KEY` environment variable

### Recommendation for Our Use Case
**MAYBE - Niche Benefits**

**Strengths**:
- Access to multiple search services in one API
- GitHub trending (useful for finding popular libraries)
- arXiv search (academic/technical papers)
- Reddit/community search for real-world usage examples
- Sitemap extraction

**Considerations**:
- Pricing unclear
- Less established than competitors
- Overlaps with other tools (web search, crawling)

**Best For**: Agencies needing unified access to multiple search services (especially GitHub, arXiv, Reddit) for diverse API research. The GitHub trending feature is particularly useful for discovering popular tools and libraries.

---

## 8. Jina AI MCP Server

### Package & Installation
- **Official Package**: `jina-ai/MCP` (remote)
- **Community Options**: `jina-mcp-tools`, `mcp-jinaai-reader`
- **Remote Server**: `https://mcp.jina.ai`

### Purpose
Search foundation platform providing URL-to-markdown conversion, web search, embeddings, and reranking for LLM applications.

### Key Features
1. **Reader (r.jina.ai)**: Convert any URL to LLM-friendly text
   - Simply prepend `https://r.jina.ai/` to any URL
   - Free, no API key required for basic use
   - Rate-limited: 20 RPM without key, 200 RPM with free key

2. **Search (s.jina.ai)**: Web search with full content extraction
   - SERP API functionality
   - Top 5 results with full content (not just snippets)
   - Must be combined with read_url for actual content

3. **Parallel Reading**: Read multiple URLs simultaneously

4. **Embeddings & Reranking**: Advanced search relevance (shared API key)

### Pricing
- **Free Tier**: 10 million tokens per new API key
- **Rate Limits Without Key**: 20 requests/minute (by IP)
- **Rate Limits With Key**: 200 requests/minute
- **Paid Pricing**: ~$0.02 per million tokens (pay-as-you-go)

**Token Sharing**: One API key valid for Reader, Embeddings, Reranking, Classifying, Fine-tuning

### API Key Requirements
- **Required**: Optional for basic use, recommended for higher limits
- **How to obtain**:
  1. Visit https://jina.ai
  2. Sign up for free API key
  3. Get 10M free tokens
- **Setup**: Set `JINA_API_KEY` environment variable (optional)

### Recommendation for Our Use Case
**YES - Highly Recommended (Best Free Option)**

**Strengths**:
- **Best free tier**: 10 million tokens is extremely generous
- Reader works without API key (rate-limited)
- Clean markdown conversion optimized for LLMs
- Search returns full content, not just snippets
- Extremely affordable at $0.02/million tokens
- One key for multiple services (embeddings, reranking)
- Simple URL prefix syntax (r.jina.ai/URL)

**Considerations**:
- Search must be combined with read_url (two-step process)
- Rate limits on free tier (20 RPM without key, 200 with key)
- Relatively new compared to established players

**Best For**: Agencies starting with API research on a budget. The generous free tier and simple URL-prefix syntax make it ideal for rapid documentation extraction. Perfect for converting API documentation pages to LLM-ready format.

---

## Comparison Table

| Tool | Primary Use | Free Tier | Paid Pricing | API Key | Best Feature | Recommendation |
|------|-------------|-----------|--------------|---------|--------------|----------------|
| **Tavily** | AI-optimized search | Limited | ~$8/1000 | Required | Search+Extract+Map+Crawl all-in-one | **YES** - Production |
| **Firecrawl** | Web scraping | 500 pages | $16/mo (3K) | Required | JS rendering, clean markdown | **YES** - Scraping |
| **Perplexity** | AI research | Unknown | Token-based | Required | Deep research with citations | MAYBE - Specialized |
| **Brave Search** | Privacy search | 2,000/mo | $3/1000 | Required | Generous free tier, lowest cost | **YES** - Budget |
| **Exa** | Semantic search | $10-20 credit | $5/1000 | Required | get_code_context_exa for APIs | **YES** - Quality |
| **Olostep** | Web scraping | Unknown | Unknown | Required | Google search + markdown | MAYBE - Unclear pricing |
| **Search1API** | Multi-service | 25K credits | Unknown | Required | GitHub/arXiv/Reddit access | MAYBE - Niche |
| **Jina AI** | Reader/Search | 10M tokens | $0.02/M tokens | Optional | Best free tier, r.jina.ai prefix | **YES** - Best free |

---

## Recommended Tool Combinations

### For Maximum Free Tier Coverage
**Total Cost: $0/month**

1. **Jina AI** - Primary documentation reader (10M free tokens)
   - Use r.jina.ai/[URL] for converting docs to markdown
   - Use s.jina.ai for search with full content

2. **Brave Search** - Web search (2,000 free queries/month)
   - Use for broad API discovery searches
   - Privacy-focused, no tracking

3. **Firecrawl** - Limited scraping (500 free pages)
   - Use for JavaScript-heavy sites
   - Save for complex documentation that Jina can't handle

**Total Free Resources**: 10M Jina tokens + 2,000 Brave searches + 500 Firecrawl pages

---

### For Production Quality Research
**Estimated Cost: $50-100/month**

1. **Exa** - Primary semantic search ($49/mo or pay-per-use)
   - Use get_code_context_exa for API discovery
   - Semantic search finds better results than keyword

2. **Tavily** - Comprehensive research ($8/1000 searches)
   - Use tavily-search for initial discovery
   - Use tavily-extract for structured data
   - Use tavily-map for site architecture
   - Use tavily-crawl for comprehensive coverage

3. **Firecrawl** - Standard plan ($83/mo for 100K credits)
   - Use for bulk documentation extraction
   - Clean markdown for LLM consumption

4. **Jina AI** - Supplementary reader (10M free tokens)
   - Use for quick URL conversions
   - Zero cost supplement

**Best For**: Agencies with budget for high-quality research requiring semantic search, comprehensive crawling, and reliable scraping.

---

### For API Documentation Focus
**Estimated Cost: $20-40/month**

1. **Exa** - Primary tool (pay-per-use ~$20/mo)
   - get_code_context_exa for finding API docs
   - research_paper_search for technical papers
   - Semantic search for better relevance

2. **Jina AI** - Documentation reader (10M free tokens)
   - Convert API doc URLs to markdown
   - Free tier sufficient for moderate use

3. **Search1API** - Multi-source search (~$20/mo estimate)
   - GitHub trending for popular tools
   - arXiv for technical specifications
   - Reddit for real-world usage patterns

4. **Brave Search** - Fallback search (2,000 free queries)
   - Zero cost backup
   - Privacy-focused

**Best For**: Agencies specifically focused on API discovery and documentation extraction with moderate budget.

---

## Implementation Priority

### Phase 1: Free Tier Foundation (Week 1)
1. Set up **Jina AI** (no key required, then free key)
2. Set up **Brave Search** (2,000 free queries)
3. Test with 10-20 API documentation URLs

### Phase 2: Enhanced Capabilities (Week 2)
4. Add **Firecrawl** (500 free pages for JS-heavy sites)
5. Test crawling complex documentation sites
6. Evaluate which paid tool provides best ROI

### Phase 3: Production (Week 3-4)
7. Choose paid tier based on needs:
   - Budget: Stick with free tiers
   - Quality: Add Exa + Tavily
   - Volume: Add Firecrawl Standard

---

## API Key Acquisition Guide

### Priority 1: Free, No Credit Card
1. **Jina AI** - https://jina.ai (10M tokens free)
   - Sign up → Get API key → 10M tokens instantly

### Priority 2: Free with Credit Card Verification
2. **Brave Search** - https://brave.com/search/api (2,000/mo free)
   - Sign up → Add card for verification (not charged) → Get key

### Priority 3: Free Trial Credits
3. **Firecrawl** - https://www.firecrawl.dev (500 pages free)
   - Sign up → Get key → 500 free credits
4. **Exa** - https://exa.ai ($10-20 free credit)
   - Sign up → Get key → Free credits applied

### Priority 4: Paid Only (Evaluate First)
5. **Tavily** - https://tavily.com
   - Sign up → Choose plan → Get key
6. **Perplexity** - Perplexity API Portal
   - Sign up → Get key → Token-based billing
7. **Olostep** - https://olostep.com
   - Contact for pricing details
8. **Search1API** - https://www.search1api.com
   - Sign up → Choose plan

---

## Final Recommendation

### For Your Deep API Documentation Research Use Case:

**Start with Free Tier (Recommended)**:
```
1. Jina AI (primary) - 10M tokens free
2. Brave Search (secondary) - 2,000 queries/month free
3. Firecrawl (specialized) - 500 pages free
```

This combination provides:
- Unlimited URL-to-markdown conversion (Jina)
- 2,000 web searches (Brave)
- 500 scraped pages for JS-heavy sites (Firecrawl)
- Total cost: $0/month

**Upgrade Path if Free Tier Insufficient**:
```
Add Exa ($49/mo or pay-per-use) for:
- get_code_context_exa (API discovery)
- Semantic search (better results)
- Code example finding
```

**Production-Ready Setup**:
```
Exa + Tavily + Firecrawl Standard
Estimated: $100-150/month
Best quality, most comprehensive
```

### Why This Approach?

1. **Cost-Effective**: Free tier handles most research needs
2. **Complementary**: Each tool excels at different tasks
3. **Scalable**: Easy to add paid tiers as needed
4. **Quality**: Jina + Brave provide excellent free foundation
5. **Specialized**: Firecrawl handles edge cases (JS sites)

The free tier combination should handle 80-90% of API documentation research needs. Only upgrade when hitting rate limits or needing semantic search quality.

---

## Sources

### Search Results
- [Perplexity MCP Documentation](https://docs.perplexity.ai/guides/mcp-server)
- [Brave Search API Pricing](https://brave.com/search/api/)
- [Tavily MCP GitHub](https://github.com/tavily-ai/tavily-mcp)
- [Firecrawl Pricing](https://www.firecrawl.dev/pricing)
- [Exa Pricing](https://exa.ai/pricing)
- [Jina AI Reader](https://jina.ai/reader/)
- [Official MCP Registry](https://github.com/modelcontextprotocol/registry)
- [Search1API GitHub](https://github.com/fatwang2/search1api-mcp)
- [Olostep MCP Server](https://github.com/olostep/olostep-mcp-server)
- [Exa MCP GitHub](https://github.com/exa-labs/exa-mcp-server)

### Tool Documentation
- [@modelcontextprotocol/server-brave-search](https://www.npmjs.com/package/@modelcontextprotocol/server-brave-search)
- [Perplexity API GitHub](https://github.com/perplexityai/modelcontextprotocol)
- [Firecrawl MCP npm](https://www.npmjs.com/package/firecrawl-mcp)
- [Jina AI MCP GitHub](https://github.com/jina-ai/MCP)
