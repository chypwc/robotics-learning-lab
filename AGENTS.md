# Project Rules

## Execution environment

1. **Authoritative checkout:** Treat `/home/maxwell/Repos/robotics_autonomous` in Ubuntu WSL2 as the repository.
2. **Run natively in WSL:** Perform repository reads, edits, Git operations, builds, tests, and renders with Linux executables and native Linux paths.
3. **Verify each batch:** Run `git diff --check`, inspect the affected diff and source region, then run the relevant test or render. Activate the repository virtual environment before Quarto executes Python blocks, and remove generated files when they are not requested deliverables.
4. **Keep textbooks read-only:** Read textbook sources from the repository-local `textbooks/` directory; never modify them.
5. **Read the project context:** Before project work, read `PLAN.md` for the programme purpose, scope, architecture, milestones, and phase outcomes, then read `CHECKLIST.md` for the current phase, active capability, ordered tasks, and evidence links. Work from `CHECKLIST.md`.

## Note writing

1. **Teacher-led notes:** Write timeless, self-contained lessons in a clear teaching voice. Define prerequisites, assumptions, units, and concepts step by step without unexplained jumps.
2. **First-draft completeness:** Define every technical term at first use. Derive each equation or result unless it is a definition or an explicitly identified prerequisite, showing the intermediate steps, assumptions, and reasoning. Do not defer missing definitions, derivations, or explanations to later review.
3. **Mathematical presentation:** Explain the mathematical model before algorithms or code, and use `$...$` for inline mathematics and `$$...$$` for display mathematics.
4. **Textbook-grounded drafting:** Before drafting any mathematical, physical, algorithmic, or theoretical learning block, consult the primary chapter routed by `textbooks/INDEX.md`. For a major concept, also consult a supporting source when it provides an independent derivation, a different modelling viewpoint, or implementation guidance. Preserve the source's dependency order and depth, map its notation to the project notation, and cite it bibliographically; do not copy its wording or follow outdated software guidance in place of current official documentation.
5. **Define notation at first use:** Define every symbol, set, space, index, superscript, subscript, and operator when it first appears. State its meaning, mathematical type or dimensions, and physical units when applicable. For a mapping or equation, identify the dimensions or spaces of its inputs and outputs; for example, if $\mathbf{A}\in\mathbb{R}^{m\times n}$ and $\mathbf{y}=\mathbf{A}\mathbf{x}$, state that $\mathbf{x}\in\mathbb{R}^n$ and $\mathbf{y}\in\mathbb{R}^m$.
6. **Unified notation:** Follow project-wide notation and map textbook notation to it; do not duplicate chapter-level notation tables.
7. **Incremental notation registry:** After completing each chapter, add only the notation first introduced by that chapter to `notes/notation.qmd`, preserving chapter order. Do not pre-populate notation for unfinished chapters, and use chapter cross-references so reordered chapters update automatically.
8. **Incremental concept glossary:** After completing and reviewing each chapter, add only its newly defined technical terms to `notes/glossary.qmd`. Keep entries alphabetical, concise, and linked to the first defining section; do not add terminology from unfinished chapters or duplicate the notation registry.
9. **Clean scope:** Omit project status, phase questions, progress markers, local source paths, and implementation-status commentary. Cite books bibliographically. Keep all live programme and capability status in `CHECKLIST.md`.
10. **Retrieval tests:** After each major concept, test recall, explanation, derivation, application, and limitations. Include cumulative chapter tests with answers or hints.
11. **Review cadence:** Write one small learning block at a time and wait for user review before continuing.
12. **Paragraph formatting:** Keep each prose paragraph on one source line; use line breaks only for headings, lists, tables, code blocks, and display mathematics.
13. **Quarto numbering:** Keep `number-sections: true` and `number-depth: 3`. Let Quarto number chapter titles, `##` sections, and `###` subsections; do not write numeric prefixes or `Step N` in headings. Leave `####` headings unnumbered by depth.
14. **Supporting sections:** Mark chapter purpose, prerequisites, dependency maps, quick tests and answers, cumulative tests, references, and supplemental checks with `{.unnumbered}` so they do not consume section numbers.
15. **Internal cross-references:** Give referenced headings stable, unique `{#sec-...}` labels and cite them with `@sec-...`; never hard-code generated section numbers.
16. **Purpose before formalism:** Introduce each concept with the concrete physical or mathematical problem it solves. Describe the situation and intended use before introducing terminology, notation, or formulas.
17. **Separate reality from representation:** Distinguish physical objects, states, and motions from their coordinate descriptions and mathematical operators; for example, distinguish turning from orientation, a vector from its coordinate column, and a configuration from its generalised coordinates.
18. **Frame-explicit explanations:** For every frame-dependent quantity, state what it describes, relative to which reference, and in which frame its components are expressed. Do not describe a quantity as measured by the body when it is only expressed along body axes.
19. **Bridge every equation:** Before an equation, state where it comes from; derive it from the preceding definitions; afterward, explain its mathematical meaning, physical interpretation, and intended use. Do not introduce formulas without a clear connection to the surrounding argument.
20. **Concrete and mathematical before abstract:** Introduce a concept through a concrete physical, geometric, or numerical example, followed by an explicit mathematical definition. Prefer equations, sets, mappings, and worked consequences over abstract verbal descriptions alone; then explain the broader interpretation and why the abstraction is useful.
21. **Contrast confusable terms:** When related terms may be confused, define them together and state their difference explicitly; for example, distinguish orientation from turning, body twist from body velocity, and active rotation from coordinate transformation.
22. **Signpost proofs:** State what a proof intends to establish and outline its logic before the algebra. When proving equality of two sets, mappings, or characterisations, show both directions and explain why each direction is necessary.
23. **Simple English:** Use simple, readable English.

## Capability workflow

1. **Dependency-gated cycle:** Move one active implementation-sized capability through learn and write → review → specify → implement and document → verify. Engineering may start when its prerequisite theory is approved and its minimum specification is ready; unrelated phase theory need not be complete.
2. **Artifact boundaries:** Create an implementation companion only when implementation begins. Keep theory and retrieval checks in learning notes, durable implementation know-how in companion notes, requirements and acceptance criteria in specifications under `docs/`, production code and deterministic checks in `ros_ws/src`, and interpreted phase or release conclusions in verification reports under `docs/reports/`. `CHECKLIST.md` records status and links to this evidence; it does not duplicate the evidence itself. Create a separate verification report for phase or release milestones, experiments, benchmarks, safety or performance claims, negative results, or results requiring interpretation.

## Document ownership

1. **Programme plan:** `PLAN.md` is the stable source for the learning programme's purpose, scope, architecture, milestone dependencies, phase learning goals, capstone products, and completion criteria. Do not put live status or task checkboxes in it.
2. **Live checklist:** `CHECKLIST.md` is the sole live progress tracker. Keep a compact programme-status table, expand only the current phase into ordered artifact-level capability tasks, name exactly one active task, and link rather than copy evidence.
3. **Rolling detail:** When a phase closes, preserve its conclusions in the owning phase verification report, reduce it to one status row in `CHECKLIST.md`, and expand the next phase there. Git history preserves completed working detail.
4. **Historical trackers:** Files marked as legacy archives are non-authoritative and must not be used to decide current work.

## Coding

1. **Learner-authored code:** Explain the purpose, mathematics, interfaces, and verification first; then provide one manageable code block per conversation for the user to write and review. Do not edit implementation @files unless explicitly requested.
2. **Necessity gate:** Add code only for a stated requirement that cannot be met more simply; avoid speculative features, abstractions, and dependencies.
3. **Traceability:** Ground every algorithmic or scientific component in a documented mathematical model. Trace infrastructure components to explicit engineering requirements.
4. **Design quality:** Keep modules single-purpose with clear names, types, units, assumptions, invariants, inputs, outputs, and failure behaviour. Keep configuration separate from logic.
5. **Verification:** Test each block against its requirements and mathematical expectations using known cases, edge cases, invariants, and integration checks where appropriate.
6. **Test value:** Prioritise tests for project logic, requirements, edge cases, invariants, public contracts, integration boundaries, and previously observed defects. Do not test unchanged language or library behaviour, trivial data storage, generated boilerplate, or simple accessors unless they form a deliberate public contract or protect against a credible regression.
7. **Reproducibility:** Pin or document dependencies, control randomness, avoid hidden state, and record the configuration required to reproduce results.
8. **Operational quality:** Validate inputs, handle failures deliberately, use safe fallbacks, and add useful logging, telemetry, and timing information where operationally necessary.
