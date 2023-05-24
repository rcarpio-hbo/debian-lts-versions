# Get Debian LTS versions

Retrieve a list of [Long Term Stable](https://wiki.debian.org/LTS) versions of Debian.

Populate a GitHub Actions output `lts` with the latest LTS versions of Debian.

### Usage

This action has three outputs: min, max and lts.

* `min` is the lowest LTS version.
* `max` is the highest LTS version.
* `lts` is a subset of active versions

```yaml
- name: Get LTS debian details
  id: debian-lts-versions
  uses: rcarpio-hbo/debian-lts-versions@1.0.0
```

Example:
```yaml
jobs:
  debian-versions:
    runs-on: ubuntu-latest
    outputs:
      lts: ${{ steps.debian-lts-versions.outputs.lts }}
    steps:
      - name: Get LTS debian details
        id: debian-lts-versions
        uses: rcarpio-hbo/debian-lts-versions@1.0.0
      - name: Test action output
        run: |
          echo "${{ steps.debian-lts-versions.outputs.min }}"
          echo "${{ steps.debian-lts-versions.outputs.max }}"
        shell: bash

  test-versions:
    runs-on: ubuntu-latest
    needs: [debian-versions]
    strategy:
      fail-fast: false
      matrix:
        version: ${{ fromJson(needs.debian-versions.outputs.lts) }}
    steps:
      - name: Test action output
        run: |
          echo "${{ matrix.version }}"
        shell: bash

```

## Reference

- GitHub Actions: [node-lts-versions](https://github.com/msimerson/node-lts-versions)

## Future

Got ideas? Contributions are welcome. Submit a PR and it will likely be accepted.
