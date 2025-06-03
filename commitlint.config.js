// commitlint.config.js
module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    // Adjust types or scopes if needed
    'type-enum': [
      2,
      'always',
      [
        'feat', 'fix', 'docs', 'style', 'refactor', 'perf',
        'test', 'chore', 'revert', 'policy', 'strategy', 'release'
      ],
    ],
    'scope-enum': [
      1,
      'always',
      [
        'vault', 'notify', 'edr', 'maturity', 'ci', 'infra',
        'growth', 'meta', 'security', 'doc', 'lint'
      ],
    ],
  },
};

