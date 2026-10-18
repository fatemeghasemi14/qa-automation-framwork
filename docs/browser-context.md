# Browser, Context and Page in Playwright

A browser context is an isolated, fresh "browser profile" with its own
cookies and login session. Tabs (pages) in the same context share that
state. Different contexts share nothing.

## Analogy
- Browser = the Chrome app
- Context = a Chrome profile (or Incognito window)
- Page = a tab

## Why it matters for testing
Each test gets a fresh context, so tests do not affect each other.