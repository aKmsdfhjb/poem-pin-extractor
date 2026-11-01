# Poem PIN Extractor — Architecture

## System flow

```mermaid
flowchart TD
 A[Receive multi-line text] --> B[Split into lines]
 B --> C[Read line index i]
 C --> D[Split current line into words]
 D --> E{Word i exists?}
 E -->|Yes| F[Append selected word length]
 E -->|No| G[Append 0]
 F --> H{More lines?}
 G --> H
 H -->|Yes| C
 H -->|No| I[Return digit sequence]
```

## Design notes

- Keep user-interface responsibilities separate from model, API and data-service responsibilities.
- Validate inputs at the application boundary and return clear error messages.
- Keep secrets and privileged credentials on the server side.
- Document the versions of data, dependencies and model artifacts used for reproducible results.
- Test the full user journey after deployment, not only the build step.

## Deployment boundary

GitHub Pages can host static HTML, CSS, JavaScript and prebuilt frontend assets. It cannot execute Python/Flask services, server-side React Router actions, private environment variables or database operations. Those parts require a separate backend or application host.
