# Custom GPT Setup Guide: SuperfeetGPT

This guide explains how to set up SuperfeetGPT as a Custom GPT in ChatGPT.

## What is SuperfeetGPT?

SuperfeetGPT is a specialized AI assistant for the Superfeet multi-region Shopify Plus eCommerce platform. It helps developers, business users, and stakeholders understand, maintain, and extend the Superfeet platform.

## Setup Instructions

### Step 1: Generate the Knowledge Pack

First, build the knowledge pack from the agent files:

```bash
python3 scripts/build_agent_pack.py --client superfeet
```

This generates:
- `dist/superfeet-knowledge-pack.md` - Single merged markdown file
- `dist/superfeet-knowledge-pack.zip` - Zipped agent/ directory

### Step 2: Create Custom GPT in ChatGPT

1. **Open ChatGPT:**
   - Go to https://chat.openai.com
   - Click "Explore GPTs" or "Create" → "GPT"

2. **Configure GPT:**
   - **Name:** SuperfeetGPT
   - **Description:** Specialized AI assistant for Superfeet's multi-region Shopify Plus eCommerce platform. Helps with theme development, metafield management, integrations, and troubleshooting.
   - **Instructions:** Upload the knowledge pack and configure behavior (see below)

3. **Upload Knowledge:**
   - Click "Add knowledge" or "Knowledge" section
   - Upload `dist/superfeet-knowledge-pack.md`
   - Or upload `dist/superfeet-knowledge-pack.zip` and extract

4. **Configure Instructions:**
   - Copy the system instructions from `agent/00-system.md`
   - Paste into the "Instructions" field
   - Add any additional behavior rules

5. **Save:**
   - Click "Save" or "Publish"
   - Choose visibility (Private, Only people with link, or Public)

## System Instructions Template

Use this as a starting point for the Custom GPT instructions:

```
You are SuperfeetGPT, a specialized AI assistant for the Superfeet multi-region Shopify Plus eCommerce platform.

Your role is to help developers, business users, and stakeholders understand, maintain, and extend the Superfeet platform.

Platform: Shopify Plus (multi-region)
Theme: CQL Propel v24.3.0
Client: Superfeet (footcare products)
Maintained by: Arcadia Digital

When answering questions:
- Reference specific documentation files and sections
- Provide actionable steps, not just explanations
- Cite sources (which doc, which section)
- Acknowledge limitations (e.g., theme code not in repo)
- Consider multi-store context (US, Canada, UK)

Always prioritize evidence from the knowledge pack over general knowledge.
```

## Testing

After setup, test SuperfeetGPT with questions from `agent/evals.yaml`:

1. "How does the Superfeet theme layout system work?"
2. "What metafields are available in the cql namespace?"
3. "How do I set up SearchSpring on a collection?"
4. "What's the workflow for making a theme change?"

## Maintenance

When updating SuperfeetGPT:

1. **Update Agent Files:**
   - Edit files in `agent/` directory
   - Update documentation as needed

2. **Rebuild Knowledge Pack:**
   ```bash
   python3 scripts/build_agent_pack.py --client superfeet
   ```

3. **Update Custom GPT:**
   - Go to Custom GPT settings
   - Upload new `dist/superfeet-knowledge-pack.md`
   - Or update individual knowledge files

4. **Test:**
   - Run test questions from `evals.yaml`
   - Verify answers are accurate and cite sources

## Alternative Platforms

### Claude (Anthropic)

1. Upload individual files from `agent/` directory
2. Or use the merged markdown file
3. Configure system prompt from `agent/00-system.md`

### Google Gemini

1. Upload knowledge files to Gemini
2. Configure with system instructions
3. Test with evaluation questions

### Cursor/VS Code

1. Reference `agent/` directory files
2. Use as context for AI coding assistants
3. Files are automatically indexed

## Troubleshooting

**Knowledge Pack Not Loading:**
- Check file size (ChatGPT has limits)
- Try splitting into multiple files
- Use the zip file and extract

**Answers Not Accurate:**
- Verify knowledge pack includes all evidence files
- Check system instructions are correct
- Test with evaluation questions

**Missing Information:**
- Update agent files with new information
- Rebuild knowledge pack
- Re-upload to Custom GPT

## Resources

- **Knowledge Pack Files:** `agent/` directory
- **Build Script:** `scripts/build_agent_pack.py`
- **Evaluation Questions:** `agent/evals.yaml`
- **System Instructions:** `agent/00-system.md`
