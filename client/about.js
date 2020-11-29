export default {
  client: {
    host: '0.0.0.0'
  },
  server: {
    current_time: Math.floor(Date.now() / 1000),
    services: [
      {
        name: 'GitHub',
        widgets: [
          {
            name: 'GitHub Account Repositories',
            description: 'List a user\'s repositories',
            params: [
              {
                username: 'Searched username'
              }
            ]
          },
          {
            name: 'GitHub Account',
            description: 'Get information about a GitHub user',
            params: [
              {
                username: 'Searched username'
              }
            ]
          }
        ]
      },
      {
        name: 'Weather',
        widgets:
        [
          {
            name: 'Weather forecast',
            description: 'Get weather forecast in 5 days',
            params: [
              {
                city: 'Searched city'
              }
            ]
          },
          {
            name: 'Weather',
            description: 'Get current weather',
            params: [
              {
                city: 'Searched city'
              }
            ]
          }
        ]
      },
      {
        name: 'YouTube',
        widgets:
          [
            {
              name: 'YouTube Channel info',
              description: 'Get a YouTube channel informations',
              params:
                [
                  {
                    name: 'Channel name'
                  }
                ]
            },
            {
              name: 'YouTube Comment',
              description: 'Comment a video',
              params:
                [
                  {
                    name: 'Video name'
                  }
                ]
            },
            {
              name: 'YouTube search',
              description: 'Search and play a video',
              params:
                [
                  {
                    name: 'Video name'
                  }
                ]
            }
          ]
      }
    ]
  }
}
