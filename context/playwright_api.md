# Playwright API Testing Context

Playwright allows API testing using request context.

Example:

```ts
import { test, expect } from '@playwright/test';

test('example', async ({ request }) => {

  const response = await request.post('/api/login', {
    data: {
      email: "user@test.com",
      password: "password123"
    }
  });

  expect(response.status()).toBe(200);

});