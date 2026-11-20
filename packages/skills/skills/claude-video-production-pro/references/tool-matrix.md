# Tool matrix and official integration notes

Use this reference when choosing a tool or describing an integration. Recheck the vendor page before quoting prices, credits, plan limits, model names, or regional availability.

## Official or documented Claude routes

- Adobe for Claude: documented connector for selected Premiere Pro, Firefly, and Creative Cloud tasks. Do not infer full After Effects timeline/keyframe automation.
- Runway MCP: official MCP route for Claude.ai/Desktop/Code; Runway Dev API and SDKs are the automation route.
- Luma MCP: official Luma MCP at `https://agents.lumalabs.ai/mcp`; Luma also provides REST/SDK workflows.
- Kling MCP: official MCP at `https://kling.ai/mcp`; also use Kling REST API for production pipelines.
- Jitter MCP beta: official experimental MCP at `https://mcp.jitter.video`; check current feature limits.
- Google Veo: use Flow manually or Vertex AI/Agent Platform programmatically. Do not label Flow a public API or native Claude connector without current official proof.
- DaVinci Resolve, Blender, Cavalry: use their documented scripting/CLI/file routes. Treat any Claude bridge as custom unless the vendor publishes an official connector.

## Decision guide

- Final edit, captions, sound, delivery variants: Premiere Pro or Resolve.
- High-control 2D/3D motion, titles, logos, VFX: After Effects, Fusion, or Blender.
- Fast AI shot ideation and B-roll: Firefly, Runway, Luma, Kling, or Veo depending on rights, motion, references, and budget.
- Interactive animation shipped inside apps: Rive.
- Procedural 2D motion: Cavalry or Motion Canvas.
- Fast collaborative social motion: Jitter.
- Color and integrated node compositing: Resolve/Fusion.
- Free/open 3D and batch rendering: Blender.

## Sources

- https://claude.com/skills
- https://helpx.adobe.com/creative-cloud/apps/integration-with-other-apps/adobe-connectors/adobe-for-claude.html
- https://developer.adobe.com/firefly-services/docs/firefly-api/
- https://docs.dev.runwayml.com/guides/mcp/
- https://docs.dev.runwayml.com/guides/using-the-api/
- https://lumalabs.ai/mcp
- https://docs.lumalabs.ai/docs/api
- https://kling.ai/app/mcp/guide
- https://app.kling.ai/global/dev/document-api/quickStart/userManual
- https://deepmind.google/models/veo/
- https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/veo-video-generation
- https://www.blackmagicdesign.com/products/davinciresolve/
- https://www.blackmagicdesign.com/products/davinciresolve/fusion
- https://www.blender.org/features/
- https://docs.blender.org/api/current/index.html
- https://jitter.video/help/en/articles/17600405-connect-jitter-to-your-ai-assistant-with-the-mcp-server
- https://rive.app/runtimes
- https://motioncanvas.io/docs/quickstart
- https://helpx.adobe.com/fonts/web/font-licensing/font-licensing.html
- https://fonts.google.com/knowledge/introducing_type/introducing_variable_fonts
- https://docs.anthropic.com/en/docs/claude-code/skills
- https://docs.anthropic.com/en/docs/claude-code/mcp
- https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector
