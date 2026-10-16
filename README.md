# Practical Engineering Problem Bank

Build practical Python engineering skills through **48 exercises across 12 topics**: APIs, queues, caches, concurrency, async I/O, streaming, recovery, and small integrated services.

**Python 3.11+ · 12 starter exercises · 0/48 complete**

This repository is a starting workspace. It contains the curriculum, original exercise briefs, acceptance criteria, and empty implementation/test folders. No exercises have been solved and no acceptance tests have been implemented.

## Navigation

- [Getting started](#getting-started)
- [Topic guide](#topic-guide)
- [Exercise order](#exercise-order)
- [Practice method](#practice-method)
- [Difficulty guide](#difficulty-guide)
- [Repository structure](#repository-structure)
- [Sources and scope](#sources-and-scope)

## Getting started

1. Use Python **3.11 or newer** and optionally create a local environment:

   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   # Windows PowerShell: .venv\Scripts\Activate.ps1
   ```

2. Start with **PE01**, then follow the **Order** column below. The first 12 rows are the workbook's starter path. Exercise IDs are stable references, not the recommended execution order.
3. Open an exercise's linked README for its full task, acceptance checks, suggested Python tools, reference, and optional follow-up. Read its prerequisites first.
4. When ready to practise, add code under that exercise's `src/` folder and tests under `tests/`. Copy the [design-note template](docs/design-note-template.md) into the exercise as `NOTES.md`.
5. Update your status, attempts, last-practised date, and notes in [the progress tracker](data/problems.csv). The README's completion count is an initial snapshot, not an automatically updated counter.

The starter repository has no third-party dependencies. Most exercises use the standard library; choose any additional tools when an exercise needs them.

## Topic guide

Each topic contains four exercises. “Start with” comes from the Topics tab; use the ordered index below for the overall learning sequence.

### T01 · API design and state machines

Classes, method contracts, validation, errors, encapsulation, valid transitions and invariants.

**Python tools:** dataclasses, enum, typing, exceptions

**Start with:** [PE01](exercises/t01-api-design-and-state-machines/pe01/README.md) · **Progress:** 0/4 complete

### T02 · Queues and backpressure

FIFO buffers, capacity, ring buffers, producer-consumer coordination, blocking and graceful shutdown.

**Python tools:** collections.deque, queue.Queue, threading.Condition

**Start with:** [PE05](exercises/t02-queues-and-backpressure/pe05/README.md) · **Progress:** 0/4 complete

### T03 · Caches and key-value stores

Lookup, ordering, eviction, versioned reads, compound updates and separating cache policy from storage.

**Python tools:** dict, OrderedDict, bisect, linked lists

**Start with:** [PE09](exercises/t03-caches-and-key-value-stores/pe09/README.md) · **Progress:** 0/4 complete

### T04 · Time, expiry and rate limits

Clock injection, deadlines, TTL, time windows, leases, renewal and exact boundary behaviour.

**Python tools:** time.monotonic, deque, heapq, callable clocks

**Start with:** [PE13](exercises/t04-time-expiry-and-rate-limits/pe13/README.md) · **Progress:** 0/4 complete

### T05 · Thread safety and coordination

Shared memory, interleavings, critical sections, mutual exclusion, signalling, lock scope and deadlocks.

**Python tools:** threading.Lock, Event, Condition, Barrier

**Start with:** [PE17](exercises/t05-thread-safety-and-coordination/pe17/README.md) · **Progress:** 0/4 complete

### T06 · Worker pools and scheduling

Futures, bounded in-flight work, dynamic tasks, deduplication, result collection and worker lifecycle.

**Python tools:** ThreadPoolExecutor, Future, as_completed, queue

**Start with:** [PE21](exercises/t06-worker-pools-and-scheduling/pe21/README.md) · **Progress:** 0/4 complete

### T07 · Async I/O and cancellation

Coroutines, tasks, await points, event-loop blocking, bounded concurrency, deadlines and cleanup.

**Python tools:** asyncio.gather, TaskGroup, Queue, Semaphore, timeout

**Start with:** [PE25](exercises/t07-async-i-o-and-cancellation/pe25/README.md) · **Progress:** 0/4 complete

### T08 · Streaming and incremental parsing

Chunk boundaries, incremental decoding, partial records, ordering, finite buffers and end-of-stream handling.

**Python tools:** iterators, generators, codecs, re, Counter

**Start with:** [PE29](exercises/t08-streaming-and-incremental-parsing/pe29/README.md) · **Progress:** 0/4 complete

### T09 · Retries and failure handling

Transient versus permanent failures, attempt budgets, backoff, idempotency, circuit breakers and dead letters.

**Python tools:** exceptions, injected clocks, random.Random, logging

**Start with:** [PE33](exercises/t09-retries-and-failure-handling/pe33/README.md) · **Progress:** 0/4 complete

### T10 · Persistence and recovery

Serialization, atomic file replacement, transaction boundaries, uniqueness constraints and restart recovery.

**Python tools:** json, pathlib, tempfile, os.replace, sqlite3

**Start with:** [PE37](exercises/t10-persistence-and-recovery/pe37/README.md) · **Progress:** 0/4 complete

### T11 · Testing, debugging and observability

Behavioural tests, fake dependencies, forced interleavings, fault injection, profiling, metrics and structured logs.

**Python tools:** unittest, unittest.mock, Barrier, logging, cProfile

**Start with:** [PE41](exercises/t11-testing-debugging-and-observability/pe41/README.md) · **Progress:** 0/4 complete

### T12 · Integrated service exercises

Combine APIs, concurrency, expiry, bounded work, recovery and instrumentation in a small running service.

**Python tools:** http.server or familiar framework; tools from T01-T11

**Start with:** [PE45](exercises/t12-integrated-service-exercises/pe45/README.md) · **Progress:** 0/4 complete

## Exercise order

Difficulty is the curriculum's training estimate. The source platform's rating is listed separately in each exercise brief and the CSV tracker. All exercises currently have status **Not started**, **0 attempts**, and no last-practised date.

| Order | Exercise | Topic | Difficulty | Starter | Prerequisites |
| ---: | --- | --- | --- | :---: | --- |
| 1 | [PE01 · 1603. Design Parking System](exercises/t01-api-design-and-state-machines/pe01/README.md) | T01 | Easy | Yes | None |
| 2 | [PE02 · JSON command adapter for a key-value store](exercises/t01-api-design-and-state-machines/pe02/README.md) | T01 | Easy | Yes | None |
| 3 | [PE05 · FIFO queue with explicit empty behaviour](exercises/t02-queues-and-backpressure/pe05/README.md) | T02 | Easy | Yes | None |
| 4 | [PE06 · 622. Design Circular Queue](exercises/t02-queues-and-backpressure/pe06/README.md) | T02 | Medium | Yes | [PE05](exercises/t02-queues-and-backpressure/pe05/README.md) |
| 5 | [PE04 · Job lifecycle manager](exercises/t01-api-design-and-state-machines/pe04/README.md) | T01 | Medium | Yes | [PE02](exercises/t01-api-design-and-state-machines/pe02/README.md), [PE05](exercises/t02-queues-and-backpressure/pe05/README.md) |
| 6 | [PE41 · Tests from a state-transition table](exercises/t11-testing-debugging-and-observability/pe41/README.md) | T11 | Easy | Yes | [PE04](exercises/t01-api-design-and-state-machines/pe04/README.md) |
| 7 | [PE09 · Bounded key-value cache](exercises/t03-caches-and-key-value-stores/pe09/README.md) | T03 | Easy | Yes | [PE02](exercises/t01-api-design-and-state-machines/pe02/README.md) |
| 8 | [PE13 · 933. Number of Recent Calls](exercises/t04-time-expiry-and-rate-limits/pe13/README.md) | T04 | Easy | Yes | [PE05](exercises/t02-queues-and-backpressure/pe05/README.md) |
| 9 | [PE14 · 1797. Design Authentication Manager](exercises/t04-time-expiry-and-rate-limits/pe14/README.md) | T04 | Medium | Yes | [PE13](exercises/t04-time-expiry-and-rate-limits/pe13/README.md) |
| 10 | [PE17 · Thread-safe counter](exercises/t05-thread-safety-and-coordination/pe17/README.md) | T05 | Easy | Yes | None |
| 11 | [PE18 · 1114. Print in Order](exercises/t05-thread-safety-and-coordination/pe18/README.md) | T05 | Easy | Yes | [PE17](exercises/t05-thread-safety-and-coordination/pe17/README.md) |
| 12 | [PE10 · 146. LRU Cache](exercises/t03-caches-and-key-value-stores/pe10/README.md) | T03 | Medium | Yes | [PE09](exercises/t03-caches-and-key-value-stores/pe09/README.md) |
| 13 | [PE25 · Async fan-out over fake I/O](exercises/t07-async-i-o-and-cancellation/pe25/README.md) | T07 | Easy | No | [PE02](exercises/t01-api-design-and-state-machines/pe02/README.md) |
| 14 | [PE29 · Exercism Word Count](exercises/t08-streaming-and-incremental-parsing/pe29/README.md) | T08 | Easy | No | None |
| 15 | [PE33 · Idempotent command handler](exercises/t09-retries-and-failure-handling/pe33/README.md) | T09 | Easy | No | [PE02](exercises/t01-api-design-and-state-machines/pe02/README.md) |
| 16 | [PE37 · Recover a JSON Lines event log](exercises/t10-persistence-and-recovery/pe37/README.md) | T10 | Easy | No | [PE02](exercises/t01-api-design-and-state-machines/pe02/README.md) |
| 17 | [PE03 · 1472. Design Browser History](exercises/t01-api-design-and-state-machines/pe03/README.md) | T01 | Medium | No | [PE02](exercises/t01-api-design-and-state-machines/pe02/README.md) |
| 18 | [PE07 · Bounded blocking queue](exercises/t02-queues-and-backpressure/pe07/README.md) | T02 | Medium | No | [PE05](exercises/t02-queues-and-backpressure/pe05/README.md), [PE17](exercises/t05-thread-safety-and-coordination/pe17/README.md), [PE18](exercises/t05-thread-safety-and-coordination/pe18/README.md) |
| 19 | [PE11 · 981. Time Based Key-Value Store](exercises/t03-caches-and-key-value-stores/pe11/README.md) | T03 | Medium | No | [PE02](exercises/t01-api-design-and-state-machines/pe02/README.md) |
| 20 | [PE15 · Per-client sliding-window rate limiter](exercises/t04-time-expiry-and-rate-limits/pe15/README.md) | T04 | Medium | No | [PE13](exercises/t04-time-expiry-and-rate-limits/pe13/README.md), [PE17](exercises/t05-thread-safety-and-coordination/pe17/README.md) |
| 21 | [PE19 · Exercism Bank Account plus local concurrency tests](exercises/t05-thread-safety-and-coordination/pe19/README.md) | T05 | Medium | No | [PE17](exercises/t05-thread-safety-and-coordination/pe17/README.md), [PE02](exercises/t01-api-design-and-state-machines/pe02/README.md) |
| 22 | [PE20 · 1115. Print FooBar Alternately](exercises/t05-thread-safety-and-coordination/pe20/README.md) | T05 | Medium | No | [PE18](exercises/t05-thread-safety-and-coordination/pe18/README.md) |
| 23 | [PE21 · Bounded parallel map](exercises/t06-worker-pools-and-scheduling/pe21/README.md) | T06 | Medium | No | [PE17](exercises/t05-thread-safety-and-coordination/pe17/README.md), [PE05](exercises/t02-queues-and-backpressure/pe05/README.md) |
| 24 | [PE22 · Atomic duplicate-work scheduler](exercises/t06-worker-pools-and-scheduling/pe22/README.md) | T06 | Medium | No | [PE21](exercises/t06-worker-pools-and-scheduling/pe21/README.md), [PE33](exercises/t09-retries-and-failure-handling/pe33/README.md) |
| 25 | [PE26 · Bounded asynchronous processing pipeline](exercises/t07-async-i-o-and-cancellation/pe26/README.md) | T07 | Medium | No | [PE25](exercises/t07-async-i-o-and-cancellation/pe25/README.md), [PE05](exercises/t02-queues-and-backpressure/pe05/README.md) |
| 26 | [PE27 · Async deadline and cancellation cleanup](exercises/t07-async-i-o-and-cancellation/pe27/README.md) | T07 | Medium | No | [PE25](exercises/t07-async-i-o-and-cancellation/pe25/README.md) |
| 27 | [PE30 · Incremental UTF-8 line parser](exercises/t08-streaming-and-incremental-parsing/pe30/README.md) | T08 | Medium | No | [PE29](exercises/t08-streaming-and-incremental-parsing/pe29/README.md), [PE05](exercises/t02-queues-and-backpressure/pe05/README.md) |
| 28 | [PE31 · Ordered results from an out-of-order stream](exercises/t08-streaming-and-incremental-parsing/pe31/README.md) | T08 | Medium | No | [PE05](exercises/t02-queues-and-backpressure/pe05/README.md), [PE21](exercises/t06-worker-pools-and-scheduling/pe21/README.md) |
| 29 | [PE34 · Retry wrapper with backoff](exercises/t09-retries-and-failure-handling/pe34/README.md) | T09 | Medium | No | [PE13](exercises/t04-time-expiry-and-rate-limits/pe13/README.md), [PE02](exercises/t01-api-design-and-state-machines/pe02/README.md) |
| 30 | [PE23 · Retrying task runner](exercises/t06-worker-pools-and-scheduling/pe23/README.md) | T06 | Medium | No | [PE21](exercises/t06-worker-pools-and-scheduling/pe21/README.md), [PE34](exercises/t09-retries-and-failure-handling/pe34/README.md) |
| 31 | [PE38 · Atomic file checkpoint](exercises/t10-persistence-and-recovery/pe38/README.md) | T10 | Medium | No | [PE37](exercises/t10-persistence-and-recovery/pe37/README.md) |
| 32 | [PE39 · Transactional idempotent ledger](exercises/t10-persistence-and-recovery/pe39/README.md) | T10 | Medium | No | [PE33](exercises/t09-retries-and-failure-handling/pe33/README.md), [PE37](exercises/t10-persistence-and-recovery/pe37/README.md) |
| 33 | [PE42 · Deterministic race reproduction](exercises/t11-testing-debugging-and-observability/pe42/README.md) | T11 | Medium | No | [PE17](exercises/t05-thread-safety-and-coordination/pe17/README.md), [PE41](exercises/t11-testing-debugging-and-observability/pe41/README.md) |
| 34 | [PE43 · Instrument a worker pool](exercises/t11-testing-debugging-and-observability/pe43/README.md) | T11 | Medium | No | [PE21](exercises/t06-worker-pools-and-scheduling/pe21/README.md), [PE41](exercises/t11-testing-debugging-and-observability/pe41/README.md) |
| 35 | [PE08 · Queue shutdown without lost work](exercises/t02-queues-and-backpressure/pe08/README.md) | T02 | Hard | No | [PE07](exercises/t02-queues-and-backpressure/pe07/README.md) |
| 36 | [PE12 · Thread-safe LRU cache with expiry](exercises/t03-caches-and-key-value-stores/pe12/README.md) | T03 | Hard | No | [PE10](exercises/t03-caches-and-key-value-stores/pe10/README.md), [PE14](exercises/t04-time-expiry-and-rate-limits/pe14/README.md), [PE17](exercises/t05-thread-safety-and-coordination/pe17/README.md) |
| 37 | [PE16 · Lease manager with renewal and stale tokens](exercises/t04-time-expiry-and-rate-limits/pe16/README.md) | T04 | Hard | No | [PE14](exercises/t04-time-expiry-and-rate-limits/pe14/README.md), [PE17](exercises/t05-thread-safety-and-coordination/pe17/README.md) |
| 38 | [PE24 · Dynamic graph crawler with reliable completion](exercises/t06-worker-pools-and-scheduling/pe24/README.md) | T06 | Hard | No | [PE21](exercises/t06-worker-pools-and-scheduling/pe21/README.md), [PE22](exercises/t06-worker-pools-and-scheduling/pe22/README.md), [PE23](exercises/t06-worker-pools-and-scheduling/pe23/README.md) |
| 39 | [PE28 · Async single-flight cache](exercises/t07-async-i-o-and-cancellation/pe28/README.md) | T07 | Hard | No | [PE25](exercises/t07-async-i-o-and-cancellation/pe25/README.md), [PE27](exercises/t07-async-i-o-and-cancellation/pe27/README.md), [PE09](exercises/t03-caches-and-key-value-stores/pe09/README.md) |
| 40 | [PE32 · Incremental streaming tokenizer](exercises/t08-streaming-and-incremental-parsing/pe32/README.md) | T08 | Hard | No | [PE30](exercises/t08-streaming-and-incremental-parsing/pe30/README.md), [PE29](exercises/t08-streaming-and-incremental-parsing/pe29/README.md) |
| 41 | [PE35 · Concurrent circuit breaker](exercises/t09-retries-and-failure-handling/pe35/README.md) | T09 | Hard | No | [PE17](exercises/t05-thread-safety-and-coordination/pe17/README.md), [PE14](exercises/t04-time-expiry-and-rate-limits/pe14/README.md), [PE34](exercises/t09-retries-and-failure-handling/pe34/README.md) |
| 42 | [PE36 · Robust work queue with retries and dead letters](exercises/t09-retries-and-failure-handling/pe36/README.md) | T09 | Hard | No | [PE04](exercises/t01-api-design-and-state-machines/pe04/README.md), [PE07](exercises/t02-queues-and-backpressure/pe07/README.md), [PE16](exercises/t04-time-expiry-and-rate-limits/pe16/README.md), [PE34](exercises/t09-retries-and-failure-handling/pe34/README.md) |
| 43 | [PE40 · Durable queue recovery](exercises/t10-persistence-and-recovery/pe40/README.md) | T10 | Hard | No | [PE36](exercises/t09-retries-and-failure-handling/pe36/README.md), [PE39](exercises/t10-persistence-and-recovery/pe39/README.md) |
| 44 | [PE44 · Diagnose a serialised worker pool](exercises/t11-testing-debugging-and-observability/pe44/README.md) | T11 | Hard | No | [PE21](exercises/t06-worker-pools-and-scheduling/pe21/README.md), [PE42](exercises/t11-testing-debugging-and-observability/pe42/README.md), [PE43](exercises/t11-testing-debugging-and-observability/pe43/README.md) |
| 45 | [PE45 · Reservation service with an HTTP adapter](exercises/t12-integrated-service-exercises/pe45/README.md) | T12 | Hard | No | [PE02](exercises/t01-api-design-and-state-machines/pe02/README.md), [PE16](exercises/t04-time-expiry-and-rate-limits/pe16/README.md), [PE19](exercises/t05-thread-safety-and-coordination/pe19/README.md), [PE33](exercises/t09-retries-and-failure-handling/pe33/README.md) |
| 46 | [PE46 · Configurable loading cache](exercises/t12-integrated-service-exercises/pe46/README.md) | T12 | Hard | No | [PE12](exercises/t03-caches-and-key-value-stores/pe12/README.md), [PE22](exercises/t06-worker-pools-and-scheduling/pe22/README.md), [PE43](exercises/t11-testing-debugging-and-observability/pe43/README.md) |
| 47 | [PE47 · Streaming inference request batcher](exercises/t12-integrated-service-exercises/pe47/README.md) | T12 | Hard | No | [PE26](exercises/t07-async-i-o-and-cancellation/pe26/README.md), [PE27](exercises/t07-async-i-o-and-cancellation/pe27/README.md), [PE15](exercises/t04-time-expiry-and-rate-limits/pe15/README.md), [PE43](exercises/t11-testing-debugging-and-observability/pe43/README.md) |
| 48 | [PE48 · Recoverable streaming processing pipeline](exercises/t12-integrated-service-exercises/pe48/README.md) | T12 | Hard | No | [PE30](exercises/t08-streaming-and-incremental-parsing/pe30/README.md), [PE36](exercises/t09-retries-and-failure-handling/pe36/README.md), [PE39](exercises/t10-persistence-and-recovery/pe39/README.md), [PE43](exercises/t11-testing-debugging-and-observability/pe43/README.md) |

## Practice method

1. **Learn.** Implement the baseline without a timer. Write tests as you add behaviour.
2. **Explain.** Describe state, invariants, failure rules, and the reason for each data structure.
3. **Extend.** Add the optional follow-up after the baseline works. A follow-up can be harder than its row rating.
4. **Rebuild.** For an interview-sized subset, rebuild in 45–60 minutes and reserve time for tests.

For each exercise, deliver **Python code, behavioural tests, and a short design note** covering API contracts, invariants, complexity, and trade-offs. Mark an exercise complete only when its acceptance checks pass and you can explain the solution. Testing starts with the first problem; T11 adds dedicated race reproduction, debugging, and instrumentation practice.

## Difficulty guide

| Level | Training scope |
| --- | --- |
| Easy | One main concept and a small API. Implement it with normal and boundary tests. |
| Medium | Several interacting operations, or a contained concurrency, timing, or failure-handling requirement. |
| Hard | Integrated concurrency and failure/recovery behaviour. Usually practise across several sessions before a timed MVP. |

## Repository structure

```text
.
├── README.md                       # Curriculum, topics, and ordered index
├── CONTRIBUTING.md                 # Conventions for future practice
├── data/
│   ├── topics.csv                  # Topic metadata and initial progress
│   ├── problems.csv                # Editable exercise progress tracker
│   └── briefs.csv                  # Full source briefs and references
├── docs/
│   ├── source.md                   # Workbook provenance and tab mapping
│   └── design-note-template.md     # Blank prompts for later notes
├── exercises/
│   ├── t01-api-design-and-state-machines/
│   │   ├── pe01/
│   │   │   ├── README.md           # Task, checks, tools, and follow-up
│   │   │   ├── src/.gitkeep        # Empty implementation workspace
│   │   │   └── tests/.gitkeep      # Empty test workspace
│   │   └── ...
│   └── ...                         # All 12 topics and 48 exercises
├── .editorconfig
└── .gitignore
```

See [practice conventions](CONTRIBUTING.md) for file naming, running future tests, and recording progress. No CI workflow is configured yet because there is no exercise code or test suite to run.

## Sources and scope

Adapted from your [Practical_Engineering_Problem_Bank.xlsx](https://docs.google.com/spreadsheets/d/1PKyqguS3699TKk1HsS9YGfqqSTuLt49X/edit) workbook, using all three tabs: **Topics**, **Problems**, and **Briefs**. See [source details](docs/source.md).

The workbook states that all listed statements are public/free; LeetCode and Exercism may require an account for submission or tracking. Custom exercises were authored for this curriculum. PE36 adapts the work-queue prompt referenced in the workbook. Linked Python documentation is reference material, not a separate exercise statement.

Source ratings describe the original exercises. Optional extensions were authored for this curriculum. The workbook records source links as checked on **2026-10-13**; this repository preserves those references without independently rechecking them.

No repository-wide license has been selected. External exercise statements and documentation remain subject to their respective source terms.
