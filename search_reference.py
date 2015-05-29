import requests
import sublime
import sublime_plugin


class SearchReferenceCommand(sublime_plugin.WindowCommand):
    base_url = 'https://www.elastic.co'
    base_keywords = ['elasticsearch']
    no_results_hits = [
        {
            'title': 'No results found...',
            'url': ''
        },
        {
            'title': 'Elasticsearch Reference | Elastic',
            'url': 'https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html'
        },
        {
            'title': 'Elasticsearch - The Definitive Guide | Elastic',
            'url': 'https://www.elastic.co/guide/en/elasticsearch/guide/current/index.html'
        },
        {
            'title': 'Hello Elasticsearch Blog (日本語) | by Kunihiko Kido',
            'url': 'https://medium.com/hello-elasticsearch'
        }
    ]

    @property
    def results_total(self):
        return self.results['total']

    @property
    def results_hits(self):
        return self.results['hits']

    @property
    def results_titles(self):
        hits = self.results_hits
        if self.is_no_results():
            hits = self.no_results_hits
        return [[hit['title'], hit['url']] for hit in hits]

    @property
    def results_urls(self):
        def make_url(url):
            if url.startswith('http') or not url:
                return url
            return self.base_url + url

        hits = self.results_hits
        if self.is_no_results():
            hits = self.no_results_hits
        return [make_url(hit['url']) for hit in hits]

    def query(self, keywords):
        return ' '.join(self.base_keywords + keywords.split())

    def search(self, keywords):
        query = self.query(keywords)
        try:
            response = requests.get(
                'https://www.elastic.co/suggest',
                params={'q': query}, timeout=3, verify=False)

        except requests.exceptions.RequestException as e:
            return sublime.error_message("Error: {0!s}".format(e))

        self.results = response.json()
        self.window.show_quick_panel(self.results_titles, self.open_url)
        sublime.status_message('Total: {}'.format(self.results_total))

    def is_no_results(self):
        if self.results_total == 0:
            return True
        return False

    def open_url(self, index):
        if index == -1:
            return

        url = self.results_urls[index]

        if not url:
            return self.run()

        self.window.run_command('open_url', {'url': url})

    def select_keywords(self, index):
        if index == -1:
            return

        self.search(SUGGEST_KEYWORDS[index])

    def run(self):
        self.window.show_quick_panel(SUGGEST_KEYWORDS, self.select_keywords)


SUGGEST_KEYWORDS = (
    '.net api',
    '_all',
    '_analyzer',
    '_boost',
    '_field_names',
    '_id',
    '_index',
    '_parent',
    '_routing',
    '_size',
    '_source',
    '_timestamp',
    '_ttl',
    '_type',
    '_uid',
    'add an index',
    'add failover',
    'adding a metric to the mix',
    'administration, monitoring, and deployment',
    'aggregation test-drive',
    'aggregations and analysis',
    'aggregations',
    'algorithmic stemmers',
    'all about caching',
    'an empty cluster',
    'analysis and analyzers',
    'analysis',
    'analytics',
    'analyze',
    'analyzers',
    'and filter',
    'api conventions',
    'apostrophe token filter',
    'application-side joins',
    'approximate aggregations',
    'array type',
    'ascii folding token filter',
    'assertions',
    'attachment type',
    'avg aggregation',
    'azure discovery',
    'backing up your cluster',
    'basic concepts',
    'batch processing',
    'best fields',
    'bool filter',
    'bool query',
    'boosting by popularity',
    'boosting filtered '',bsets',
    'boosting query clauses',
    'boosting query',
    'breaking changes',
    'buckets inside buckets',
    'buckets',
    'building bar charts',
    'bulk api',
    'bulk udp api',
    'cache',
    'caching geo-filters',
    'calculating percentiles',
    'capacity planning',
    'cardinality aggregation',
    'cat aliases',
    'cat allocation',
    'cat api',
    'cat apis',
    'cat count',
    'cat fielddata',
    'cat health',
    'cat indices',
    'cat master',
    'cat nodes',
    'cat pending tasks',
    'cat plugins',
    'cat recovery',
    'cat segments',
    'cat shards',
    'cat thread pool',
    'changing settings dynamically',
    'changing similarities',
    'character filters',
    'cheaper in bulk',
    'checking whether a document exists',
    'children aggregation',
    'choosing a stemmer',
    'cjk bigram token filter',
    'cjk width token filter',
    'classic token filter',
    'classic tokenizer',
    'clear cache',
    'closer is better',
    'closing thoughts',
    'cluster apis',
    'cluster health',
    'cluster reroute',
    'cluster state',
    'cluster stats',
    'cluster update settings',
    'cluster',
    'clusters are living, breathing creatures',
    'combining filters',
    'combining queries with filters',
    'combining queries',
    'combining the two',
    'common grams token filter',
    'common options',
    'common terms query',
    'common_grams token filter',
    'completion suggester',
    'complex core field types',
    'compound word token filter',
    'conclusion',
    'config mappings',
    'configuration management',
    'configuration',
    'configuring analyzers',
    'configuring language analyzers',
    'constant score query',
    'context suggester',
    'controlling analysis',
    'controlling memory use and latency',
    'controlling relevance',
    'controlling stemming',
    'coping with failure',
    'core types',
    'count api',
    'create an index',
    'create index',
    'creating a new document',
    'creating an index',
    'creating, indexing, and deleting a document',
    'cross-fields entity search',
    'cross-fields queries',
    'custom _all fields',
    'custom analyzer',
    'custom analyzers',
    'customizing dynamic mapping',
    'data in, data out',
    'date format',
    'date histogram aggregation',
    'date histogram facet',
    'date range aggregation',
    'dates without years',
    'dealing with conflicts',
    'dealing with human language',
    'dealing with null values',
    'default mapping',
    'delete an index',
    'delete api',
    'delete by query api',
    'delete index',
    'delete mapping',
    'deleting a document',
    'deleting an index',
    'deleting documents',
    'delimited payload token filter',
    'denormalization and concurrency',
    'denormalizing your data',
    'deprecations',
    'designing for scale',
    'dictionary stemmers',
    'directory layout',
    'dis max query',
    'discovery',
    'distributed document store',
    'distributed nature',
    'distributed search execution',
    'divide and conquer',
    'doc values',
    'document apis',
    'document metadata',
    'document oriented',
    'don’t touch these settings!',
    'dynamic mapping',
    'dynamically updatable indices',
    'ec2 discovery',
    'edge ngram token filter',
    'edge ngram tokenizer',
    'elision token filter',
    'empty search',
    'exact values ver'',s full text',
    'exact-value fields',
    'executing aggregations',
    'executing filters',
    'executing searches',
    'exists filter',
    'expand or contract',
    'explain api',
    'explain',
    'exploring your cluster',
    'exploring your data',
    'extended example',
    'extended stats aggregation',
    'facets',
    'faking index per user with aliases',
    'fetch phase',
    'field collapsing',
    'field data fields',
    'field data formats',
    'field data',
    'field highlight order',
    'field-centric queries',
    'fielddata filtering',
    'fielddata',
    'fields',
    'file descriptors and mmap',
    'filter aggregation',
    'filter bucket',
    'filter facets',
    'filter order',
    'filtered query',
    'filtering by geo-point',
    'filtering queries and aggregations',
    'filters aggregation',
    'filters',
    'finding associated words',
    'finding children by their parents',
    'finding distinct counts',
    'finding exact values',
    'finding multiple exact values',
    'finding parents by their children',
    'finding your feet',
    'flush',
    'formatting synonyms',
    'from / size',
    'full-body search',
    'full-text search',
    'function score query',
    'function_score query',
    'fuzziness',
    'fuzzy like this field query',
    'fuzzy like this query',
    'fuzzy match query',
    'fuzzy query',
    'gateway',
    'geo bounding box filter',
    'geo bounds aggregation',
    'geo distance aggregation',
    'geo distance facets',
    'geo distance filter',
    'geo distance range filter',
    'geo point type',
    'geo polygon filter',
    'geo shape type',
    'geo-aggregations',
    'geo-points',
    'geo-shape filters and caching',
    'geo-shapes',
    'geo_bounding_box filter',
    'geo_bounds aggregation',
    'geo_distance aggregation',
    'geo_distance filter',
    'geohash cell filter',
    'geohash grid aggregation',
    'geohash_cell filter',
    'geohash_grid aggregation',
    'geohashes',
    'geolocation',
    'geoshape filter',
    'geoshape query',
    'get api',
    'get field mapping',
    'get index',
    'get mapping',
    'get settings',
    'get transformed',
    'getting started with languages',
    'getting started',
    'global aggregation',
    'glossary of terms',
    'google compute engine discovery',
    'grandparents and grandchildren',
    'groovy api',
    'handling relationships',
    'hardware',
    'has child filter',
    'has child query',
    'has parent filter',
    'has parent query',
    'heap: sizing and swapping',
    'high-level concepts',
    'highlighting our searches',
    'highlighting',
    'histogram aggregation',
    'histogram facets',
    'how match uses bool',
    'how primary and replica shards interact',
    'html strip char filter',
    'http',
    'hunspell stemmer',
    'hunspell token filter',
    'icu analysis plugin',
    'icu_tokenizer',
    'identifying words',
    'ids filter',
    'ids query',
    'ignoring tf/idf',
    'immutable transformation',
    'important configuration changes',
    'improving performance',
    'in that case',
    'index aliases and zero downtime',
    'index aliases',
    'index and query a document',
    'index api',
    'index boost',
    'index management',
    'index modules',
    'index pattern',
    'index request',
    'index settings',
    'index shard allocation',
    'index slow log',
    'index stats',
    'index templates',
    'index-time optimizations',
    'index-time search-as-you-type',
    'indexing a document',
    'indexing employee documents',
    'indexing geo-shapes',
    'indexing parents and children',
    'indexing performance tips',
    'indices apis',
    'indices exists',
    'indices filter',
    'indices query',
    'indices recovery',
    'indices segments',
    'indices stats',
    'indices',
    'inner hits',
    'inside a shard',
    'installation',
    'installing elasticsearch',
    'installing the icu plug-in',
    'integration tests',
    'intrinsic sorts',
    'introducing the query language',
    'inverted index',
    'ip type',
    'ipv4 range aggregation',
    'java api',
    'java testing framework',
    'java virtual machine',
    'javascript api',
    'kagillion shards',
    'keep types token filter',
    'keep words token filter',
    'keyword analyzer',
    'keyword marker token filter',
    'keyword repeat token filter',
    'keyword tokenizer',
    'kstem token filter',
    'language analyzers',
    'lat/lon formats',
    'length token filter',
    'letter tokenizer',
    'life inside a cluster',
    'limit filter',
    'limit token count token filter',
    'limiting memory usage',
    'list all indexes',
    'living in a unicode world',
    'local gateway',
    'logging',
    'looking at time',
    'lowercase token filter',
    'lowercase tokenizer',
    'lucene’s practical scoring function',
    'making changes persistent',
    'making text searchable',
    'manipulating relevance with query structure',
    'mapper',
    'mapping and analysis',
    'mapping char filter',
    'mapping geo-shapes',
    'mapping geohashes',
    'mapping',
    'marvel for monitoring',
    'match all filter',
    'match all query',
    'match query',
    'max aggregation',
    'memcached',
    'merge',
    'meta',
    'metrics',
    'migrating to aggregations',
    'min aggregation',
    'min_score',
    'minimum should match',
    'missing aggregation',
    'missing filter',
    'mixed-language fields',
    'mixing it up',
    'modeling your data',
    'modifying your data',
    'modules',
    'monitoring individual nodes',
    'monitoring',
    'more like this api',
    'more like this query',
    'more-complicated searches',
    'most fields',
    'most important queries and filters',
    'multi get api',
    'multi match query',
    'multi search api',
    'multi term query rewrite',
    'multi termvectors api',
    'multi-fields',
    'multi-index, multitype',
    'multi_match query',
    'multidocument patterns',
    'multifield search',
    'multiple indices',
    'multiple query strings',
    'multivalue fields',
    'multiword queries',
    'multiword synonyms and phrase queries',
    'named queries and filters',
    'near real-time search',
    'nested aggregation',
    'nested aggregations',
    'nested filter',
    'nested object mapping',
    'nested objects',
    'nested query',
    'nested type',
    'network settings',
    'next steps',
    'ngram token filter',
    'ngram tokenizer',
    'ngrams for compound words',
    'ngrams for partial matching',
    'node level settings related to shadow replicas',
    'node',
    'nodes hot_threads',
    'nodes info',
    'nodes shutdown',
    'nodes stats',
    'normalization token filter',
    'normalizing tokens',
    'not filter',
    'not quite not',
    'object type',
    'one big user',
    'one final modification',
    'one language per document',
    'one language per field',
    'open / close index api',
    'optimistic concurrency control',
    'optimize',
    'or filter',
    'pagination',
    'parameterized tests',
    'parameters',
    'parent-child mapping',
    'parent-child relationship',
    'partial matching',
    'partial updates to a document',
    'partial updates to documents',
    'path hierarchy tokenizer',
    'pattern analyzer',
    'pattern capture token filter',
    'pattern replace char filter',
    'pattern replace token filter',
    'pattern tokenizer',
    'pending cluster tasks',
    'pending tasks',
    'percentile ranks aggregation',
    'percentiles aggregation',
    'percolator',
    'perl api',
    'phonetic matching',
    'phonetic token filter',
    'php api',
    'phrase matching',
    'phrase search',
    'phrase suggester',
    'pitfalls of mixing languages',
    'pluggable similarity algorithms',
    'plugins',
    'porter stem token filter',
    'post filter',
    'post-deployment',
    'postcodes and structured data',
    'practical considerations',
    'preference',
    'prefix filter',
    'prefix query',
    'preloading fielddata',
    'preventing combinatorial explosions',
    'production deployment',
    'pros and cons of stopwords',
    'proximity for relevance',
    'proximity matching',
    'put mapping',
    'python api',
    'queries and filters',
    'queries',
    'query dsl',
    'query facets',
    'query filter',
    'query phase',
    'query string query',
    'query',
    'query-time boosting',
    'query-time search-as-you-type',
    'querying a nested object',
    'querying geo-shapes',
    'querying with indexed shapes',
    'random scoring',
    'randomized testing',
    'range aggregation',
    'range facets',
    'range filter',
    'range query',
    'ranges',
    'recap',
    'reducing memory usage',
    'reducing words to their root form',
    'refresh',
    'regexp filter',
    'regexp query',
    'reindexing your data',
    'relevance is broken!',
    'relevance tuning is the last 10%',
    'relocation',
    'replica shards',
    'repositories',
    'request body search',
    'rescoring',
    'restoring from a snapshot',
    'retiring data',
    'retrieving a document',
    'retrieving multiple documents',
    'return values',
    'returning empty buckets',
    'reverse nested aggregation',
    'reverse token filter',
    'revisit this list before production',
    'rolling restarts',
    'root object type',
    'routing a document to a shard',
    'ruby api',
    'running as a service on linux',
    'running as a service on windows',
    'running elasticsearch',
    'scale horizontally',
    'scale is not infinite',
    'scan and scroll',
    'scoping aggregations',
    'scoring fuzziness',
    'scoring with scripts',
    'script fields',
    'script filter',
    'scripted metric aggregation',
    'scripting',
    'scroll',
    'search apis',
    'search exists api',
    'search in depth',
    'search lite',
    'search options',
    'search requests',
    'search shards api',
    'search template',
    'search type',
    'search with query dsl',
    'search',
    'searching—the basic tools',
    'segment merging',
    'setup',
    'shadow replica indices',
    'shard overallocation',
    'shard query cache',
    'shard states',
    'shared index',
    'shingle token filter',
    'significant terms aggregation',
    'significant terms',
    'significant_terms demo',
    'similarity module',
    'simple analyzer',
    'simple query string query',
    'single query string',
    'snapshot and restore',
    'snowball analyzer',
    'snowball token filter',
    'solving concurrency is'',es',
    'sort',
    'sorting and collations',
    'sorting and relevance',
    'sorting based on "deep" metrics',
    'sorting by a metric',
    'sorting by distance',
    'sorting by nested fields',
    'sorting multivalue buckets',
    'sorting',
    'source filtering',
    'span first query',
    'span multi term query',
    'span near query',
    'span not query',
    'span or query',
    'span term query',
    'standard analyzer',
    'standard token filter',
    'standard tokenizer',
    'statistical facet',
    'stats aggregation',
    'stats and info apis',
    'status',
    'stemmer override token filter',
    'stemmer token filter',
    'stemming in situ',
    'stop analyzer',
    'stop token filter',
    'stopwords and performance',
    'stopwords and phrase queries',
    'stopwords and relevance',
    'stopwords',
    'stopwords: performance ver'',s precision',
    'store',
    'string sorting and multifields',
    'structured search',
    'suggesters',
    'sum aggregation',
    'symbol synonyms',
    'synonym token filter',
    'synonyms and the analysis chain',
    'synonyms',
    'system and settings',
    'talking to elasticsearch',
    'template query',
    'term filter',
    'term query',
    'term suggester',
    'term vectors',
    'term-based ver'',s full-text',
    'terms aggregation',
    'terms facet',
    'terms filter',
    'terms query',
    'terms stats facet',
    'testing',
    'text scoring in scripts',
    'thai tokenizer',
    'the closer, the better',
    'the definitive guide',
    'the empty search',
    'the match query',
    'the root object',
    'the search api',
    'the sky’s the limit',
    'the unit of scale',
    'theory behind relevance scoring',
    'thread pool',
    'thrift',
    'tidying up input text',
    'time-based data',
    'token filters',
    'tokenizers',
    'top children query',
    'top hits aggregation',
    'transform',
    'translog',
    'transport client ver'',s node client',
    'transport tracer',
    'transport',
    'tribe node',
    'trim token filter',
    'truncate token filter',
    'tuning best fields queries',
    'tutorial conclusion',
    'type filter',
    'types and mappings',
    'types exists',
    'types',
    'typoes and mispelings',
    'uax email url tokenizer',
    'understanding the price clause',
    'unicode case folding',
    'unicode character folding',
    'unique token filter',
    'unit tests',
    'update api',
    'update indices settings',
    'updating a whole document',
    'updating documents',
    'upgrade',
    'upgrading',
    'uppercase token filter',
    'uri search',
    'url-based access control',
    'user-based data',
    'using language analyzers',
    'using stopwords',
    'using synonyms',
    'using the elasticsearch test classes',
    'validate api',
    'validating queries',
    'value count aggregation',
    'version',
    'warmers',
    'what is a document?',
    'what is relevance?',
    'whitespace analyzer',
    'whitespace tokenizer',
    'why randomized testing?',
    'wildcard and regexp queries',
    'wildcard query',
    'word delimiter token filter',
    'you have an accent',
    'you know, for search…',
    'zen discovery',
)
