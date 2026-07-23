# Project Rules

1. **Mathematics first:** Ground every algorithmic or scientific script in a documented mathematical model. Infrastructure scripts must trace to an explicit engineering requirement.
2. **LaTeX mathematics:** Use LaTeX syntax in Markdown: `$...$` for inline equations and `$$...$$` for display equations.
3. **Lecture-note standard:** Keep learning documents self-contained, compilable, and step-by-step. Define notation, units, assumptions, and prerequisites clearly; show derivations without unexplained jumps.
4. **Retrieval tests:** After each major concept, provide a short test covering recall, explanation, derivation, application, and limitations. Include cumulative chapter tests and answers or hints.
5. **Engineering quality:** Use clear requirements and interfaces, modular code, configuration, tests, telemetry, failure handling, reproducible environments, and documented verification.
6. **Textbook grounding:** When mathematical, physical, algorithmic, or theoretical grounding is unclear, consult C:/Users/chien/Documents/Repos/textbooks before writing.
7. **Unified notation:** Establish and follow project-wide notation across all notes; map textbook notation to it when necessary.
8. **Clean notes:** Cite books by bibliographic location, never by local file path, and keep progress tracking only in CHECKLIST.md.
9. **Review cadence:** Write notes one small block at a time and wait for user review before continuing.
10. **Learner-authored code:** Explain the purpose, mathematics, interfaces, and verification first; then provide one manageable code block per conversation for the user to write and review. Do not edit implementation files unless explicitly requested.
11. **Necessity gate:** Add code only for a stated requirement that cannot be met more simply; avoid speculative features, abstractions, and dependencies.
12. **Traceable design:** Keep modules single-purpose with clear names, types, units, assumptions, invariants, inputs, outputs, and failure behavior. Keep configuration separate from logic.
13. **Verification:** Test each block against requirements and mathematical expectations using known cases, edge cases, invariants, and integration checks where appropriate.
14. **Reproducibility and observability:** Pin or document dependencies, control randomness, avoid hidden state, validate inputs, handle errors deliberately, and add useful logging or telemetry where operationally necessary.
