module.exports = {
    reactStrictMode: true,
    env: {
      API_URL: process.env.API_URL || 'http://localhost:8000/api',
    },
    async headers() {
      return [
        {
          source: '/api/:path*',
          headers: [
            { key: 'Access-Control-Allow-Credentials', value: 'true' },
            { key: 'Access-Control-Allow-Origin', value: '*' },
            { key: 'Access-Control-Allow-Methods', value: 'GET,OPTIONS,PATCH,DELETE,POST,PUT' },
          ],
        },
      ]
    },
  }