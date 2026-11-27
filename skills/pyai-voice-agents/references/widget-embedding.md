# Add a click-to-talk voice assistant to a website

The PyAI managed widget adds a button visitors can click to speak with an assistant on the page. It handles microphone permission, playback and interruption. The page needs HTTPS and a script tag.

## Evaluate the recorded example

**No account, microphone, SDK or live session is required to evaluate the recording.** Open the [public recording player](https://pyai-voice-demo-wfls74alya-uc.a.run.app/managed-widget/start#listen) and press Play under the recorded example. Opening that page loads the controls. Playing the saved recording uses zero visitor sessions. The separate talk button starts a live conversation when the visitor grants microphone access.

## First implementation step

To deploy your own widget, you need a PyAI project. Follow the [website widget setup guide](https://docs.pyai.com/guides/website-voice-widget).

In your intended PyAI project, select or create an agent with the product facts it should answer from. Open **Website & phone**, enter the exact HTTPS origin of your site and set the daily session limits for the widget and each visitor IP. Preview the settings and embed. After the site owner approves publication, copy the generated snippet into the page.

This is the shape of the embed in the verified example. Use the snippet from your own published widget.

```html
<script src="https://cdn.pyai.com/widget/v12.1/pyai-widget.js"
        data-widget="YOUR_PUBLIC_WIDGET_ID" async></script>
```

An existing widget’s snippet is also available through a read-only MCP lookup. Verify the project with `whoami`, then use `list_published_website_widgets` with `widgets:read`. Keep project credentials off the page.

Starting a voice session streams microphone audio to PyAI and uses project allowance. Daily session counts cannot enforce a hard total spend cap. If visitor audio must stay on-device, the hosted widget cannot satisfy the request.

## What the example verifies

A synthetic visitor asked a product question, interrupted the spoken answer and asked to save one fictional enquiry. The backend recorded one enquiry, and the visitor heard the confirmation. The walkthrough includes the HTML, server action and receipt check. [Reproduce the managed widget example](https://raw.githubusercontent.com/atomsai/pyai-speech-integrations/main/ai-sdk/web/MANAGED-WIDGET.md)
