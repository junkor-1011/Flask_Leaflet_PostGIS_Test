Note
=========


## when update env

- `install_packages.yml`
    - with options:  https://docs.conda.io/projects/conda/en/latest/commands/update.html 
```
conda update env -f install_packages.yml
```

- 使うパッケージをなるべく必要最低限で書いていく
    - 明示的にimportするものとバージョンに条件があるものをメインで記述
- `conda env export`で生成されたymlファイルを指定することで、バージョンやビルドを固定したものをインストール出来る
    - *ただし、`name`と`prefix`は消すか適切な値に直しておくこと*

## when create env
- `create_environment_dev.yml`
```
conda env create -f create_environment_dev.yml
```
- `name`の項目を書いておく以外は基本的に↑と同じ

