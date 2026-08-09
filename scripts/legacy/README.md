# Legacy Scripts (Deprecated)

These scripts were built against the abandoned v3.0 rich JSON schema (`practical_metrics`, `scenarios`, `anti_patterns`, `code_review_checklist`, `context_qualifiers`, `implementation_roadmap`, etc.) that was never successfully implemented because it risked inventing data not present in the source books.

**Status:** Superseded by the LLM-driven Pass 4 procedure in `reference/pass-4-json-generation.md`.

**Do not use these to regenerate 05_llm_instructions.json going forward.** They are kept for:
- Historical reference (understanding earlier design iterations)
- Emergency fallback (if LLM Pass 4 procedure fails for some reason)
- Potential future reference if the rich schema is properly sourced from books

## Files

- `generate_llm_instructions.py` — Base JSON generator (v3.0, never fully implemented)
- `generators_clean_architecture.py` — Specialized generator for Clean Architecture (hardcoded book-specific content)
- `generator_real_data.py` — Alternate "real data only" generator lineage
- `generator_smart_links.py` — Linking strategy experiments
- `parser_real_data.py` — Markdown parsing for "real data" approach

## Why Deprecated

These scripts:
1. Use regex pattern-matching on markdown headers (`## PRINCIPLE N:`)
2. Cannot handle Russian-language headers (`### Идея N:`, `## ИДЕЯ N:`, `## ПРИНЦИП N:`)
3. Cannot handle non-header-based principle organization (e.g., `martin-clean-code`'s chapter-based structure)
4. Do not translate content (just hardcode `"language": "English"` regardless of actual markdown language)
5. Generate empty fields due to paragraph-split bugs
6. Are designed around the v3.0 rich schema that was abandoned

## Current Approach

See `reference/pass-4-json-generation.md` — LLM reads 00-04, understands and links content by meaning (not regex), translates to English, writes JSON in the lean schema.
