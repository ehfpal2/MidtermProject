## Quick orientation

This repo is a small Streamlit learning app that demonstrates conversions between decimal and binary numbers.

- Primary entry: `streamlit_app.py` — page routing is driven by query params (e.g. `?page=change1` / `change2`) and uses `st.query_params = {"page": "..."}` + `st.experimental_rerun()` to navigate.
- Additional pages: `pages/change1.py`, `pages/change2.py` — each contains the UI and session-state logic for one conversion direction.
- Dependencies: listed in `requirements.txt` (Streamlit only in this project).

## Why this structure

- The app is intentionally single-file entry + small page modules for teaching. Navigation is not using Streamlit's multi-page app system but manual query-params and reruns. AI agents should respect this pattern when adding pages or linking between them.

## Run / debug quickly

- Recommended (interactive):

  ```bash
  pip install -r requirements.txt
  streamlit run streamlit_app.py
  ```

- Don't run the file directly with `python streamlit_app.py`. Doing so will print warnings like "missing ScriptRunContext" and session-state will not work. Always use `streamlit run` so Streamlit provides the ScriptRunContext and proper runtime.

## Key code patterns to follow

- Navigation: `st.query_params = {"page": "change1"}` then `st.experimental_rerun()` — keep using query params if you add pages so the same pattern remains consistent.
- Session state usage: pages rely heavily on `st.session_state` for persistent values (random seeds, user inputs, bits arrays). When resetting state, the code either clears keys or calls `st.experimental_rerun()` / `st.rerun()` accordingly. Use existing keys (examples: `decimal`, `bits`, `bit_len`, `binary`, `user_weights`).
- UI customization: small inline CSS via `st.markdown(..., unsafe_allow_html=True)` is used to style buttons and inputs. Keep any added styles minimal and scoped to avoid global breakage.

## Tests & checks

- There are no automated tests or CI in the repo. Quick local checks:

  - Verify no "missing ScriptRunContext" warnings by running with `streamlit run`.
  - Reloading/navigating should preserve `st.session_state` values between reruns when using `streamlit run`.

## Common pitfalls (raised by running logs)

- Running `python streamlit_app.py` directly produces repeated "missing ScriptRunContext" warnings and breaks session state. The fix is to run with the Streamlit runner as shown above.

## Examples and references

- To add a new page follow `pages/change1.py` and `pages/change2.py`:
  - initialize session keys with `if 'key' not in st.session_state: st.session_state.key = <default>`
  - use `st.columns()` for bit UI and `st.button(..., key=...)` when multiple similar buttons are created

## If you modify runtime behaviour

- If you switch to Streamlit's built-in multi-page support (placing multiple scripts under top-level `pages/`), update `streamlit_app.py` routing or remove the query-param navigation accordingly. Ensure session keys remain consistent across modules.

---

If anything above is unclear or you'd like the file to include additional details (example commands for Docker, VS Code debug config, or a short code snippet for adding a new page), tell me what to add and I'll update this file.
