# SHIFT
## 環境
![exampleenvironment](https://user-images.githubusercontent.com/9310683/51794411-df72a180-2215-11e9-82f5-48bb6ccd6dd4.png)

ポイント
> 知ったかぶりWindowsドメインが環境に影響します。ドメイン構築している場合は、NICの設定を忘れずに。  
> ホストオンリーは操作用です。NICをちょこちょこいじるので、環境に関係ない別ルートとして利用します。

Exampleとしての環境は、[Draw.io](https://www.draw.io)にて作成  
./Doc/ExampleEnvironment.xml  
Githubとサービス連携できますので、Draw.ioからSHIFTのリポジトリにアクセスできます。

## 実行
とりあえず実行用
~~~
cd OracleVM_edi
ansible-playbook -i hosts/oracleVM/ site.yml
~~~

ステージの考えを取り込んだので、`OracleVM_edi`自体も要変更。
