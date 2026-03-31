# Superfeet Knowledge Pack

This directory contains the **SuperfeetGPT** knowledge pack - a curated set of documentation and evidence files designed to enable an AI assistant to help with Superfeet platform questions.

## What This Is

A **Client Knowledge Pack** is a structured collection of:
- **System instructions** - How the AI should behave
- **Client overview** - Business and technical context
- **Architecture maps** - Theme, data, and integration structures
- **Runbooks** - Common workflows and troubleshooting
- **Evidence files** - Curated source files to reference

## Structure

```
agent/
├── README.md                    # This file
├── 00-system.md                 # AI system instructions
├── 10-client-overview.md        # Superfeet platform overview
├── 20-theme-map.md              # Theme architecture mental model
├── 30-data-model.md             # Metafields and data structures
├── 40-integrations-map.md       # Third-party app inventory
├── 50-runbooks.md               # Workflows and troubleshooting
├── index.json                   # Machine-readable knowledge map
├── index.schema.json            # Index validation schema
├── evidence-manifest.json       # Files to inline in final pack
├── tools-manifest.yaml          # Tool capabilities
├── evals.yaml                   # Test questions
└── CUSTOM_GPT_SETUP.md         # Platform setup instructions
```

## Building the Pack

Run the build script to generate the final knowledge pack:

```bash
python3 scripts/build_agent_pack.py --client superfeet
```

This generates:
- `dist/superfeet-knowledge-pack.md` - Single merged markdown file
- `dist/superfeet-knowledge-pack.zip` - Zipped agent/ directory

## Using the Pack

**For ChatGPT/Custom GPT:**
1. Upload `dist/superfeet-knowledge-pack.md` as a knowledge file
2. Or upload `dist/superfeet-knowledge-pack.zip` and extract

**For Claude/Gemini:**
1. Upload individual files from `agent/` directory
2. Or use the merged markdown file

**For Cursor/VS Code:**
1. Reference files in `agent/` directory
2. Use as context for AI coding assistants

## Maintenance

When updating the pack:
1. Edit files in `agent/` directory
2. Update `evidence-manifest.json` if adding new evidence files
3. Rebuild the pack: `python3 scripts/build_agent_pack.py --client superfeet`
4. Test with questions in `evals.yaml`

## Source Documentation

This pack is distilled from:
- `README.md` - Platform overview
- `docs/theme-architecture-v2.md` - Theme structure
- `docs/technical-user-guide-v2.md` - Development workflows
- `docs/data-guide.md` - Metafields reference
- `docs/integrations.md` - App documentation
- `docs/business-user-guide.md` - Business workflows
