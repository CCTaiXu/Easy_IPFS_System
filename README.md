### 1. 安装 IPFS

1. **下载 IPFS**：
   从 [IPFS 官方网站](https://ipfs.io/) 下载适用于 Windows 的 IPFS 发行版，并将其解压到你的工作目录，例如 `C:\Apps\kubo_v0.30.0_windows-amd64\kubo`。

2. **将 IPFS 二进制文件添加到系统 PATH**：
   将 IPFS 可执行文件路径添加到系统的 PATH 环境变量中，以便在命令行中全局访问 IPFS 命令。

### 2. 初始化和配置 IPFS 节点

1. **创建存储路径**：
   为每个节点创建单独的存储路径，例如 `C:\Apps\.ipfs_node1` 和 `C:\Apps\.ipfs_node2`。

   ```powershell
   mkdir C:\Apps\.ipfs_node1
   mkdir C:\Apps\.ipfs_node2
   ```

2. **初始化每个节点**：
   依次设置 `IPFS_PATH` 环境变量，并初始化每个节点。

   ```powershell
   cd C:\Apps\kubo_v0.30.0_windows-amd64\kubo

   $env:IPFS_PATH="C:\Apps\.ipfs_node1"
   .\ipfs init

   $env:IPFS_PATH="C:\Apps\.ipfs_node2"
   .\ipfs init
   ```

3. **修改配置文件**：
   确保每个节点的配置文件使用不同的端口。编辑 `C:\Apps\.ipfs_node1\config` 和 `C:\Apps\.ipfs_node2\config` 文件。

   **节点 1** 配置文件（`C:\Apps\.ipfs_node1\config`）：

   ```json
   {
     "Addresses": {
       "Swarm": [
         "/ip4/0.0.0.0/tcp/4001",
         "/ip6/::/tcp/4001",
         "/ip4/0.0.0.0/udp/4001/quic-v1",
         "/ip6/::/udp/4001/quic-v1"
       ],
       "API": "/ip4/127.0.0.1/tcp/5001",
       "Gateway": "/ip4/127.0.0.1/tcp/8080"
     }
   }
   ```

   **节点 2** 配置文件（`C:\Apps\.ipfs_node2\config`）：

   ```json
   {
     "Addresses": {
       "Swarm": [
         "/ip4/0.0.0.0/tcp/4002",
         "/ip6/::/tcp/4002",
         "/ip4/0.0.0.0/udp/4002/quic-v1",
         "/ip6/::/udp/4002/quic-v1"
       ],
       "API": "/ip4/127.0.0.1/tcp/5002",
       "Gateway": "/ip4/127.0.0.1/tcp/8081"
     }
   }
   ```

### 3. 启动 IPFS 节点

1. **启动节点 1**：

   ```powershell
   $env:IPFS_PATH="C:\Apps\.ipfs_node1"
   .\ipfs daemon
   ```

2. **启动节点 2**：

   ```powershell
   $env:IPFS_PATH="C:\Apps\.ipfs_node2"
   .\ipfs daemon
   ```

### 4. 连接节点

1. **获取节点 1 的地址**：

   ```powershell
   $env:IPFS_PATH="C:\Apps\.ipfs_node1"
   .\ipfs id
   ```

   你会看到类似如下的输出：

   ```json
   {
     "ID": "12D3KooWBUysoAjQjwne3ua8uki4tL6A8p6fLctra5L1WDeNLRex",
     "Addresses": [
       "/ip4/127.0.0.1/tcp/4001/p2p/12D3KooWBUysoAjQjwne3ua8uki4tL6A8p6fLctra5L1WDeNLRex"
     ]
   }
   ```

2. **在节点 2 上连接到节点 1**：

   ```powershell
   $env:IPFS_PATH="C:\Apps\.ipfs_node2"
   .\ipfs swarm connect /ip4/127.0.0.1/tcp/4001/p2p/12D3KooWBUysoAjQjwne3ua8uki4tL6A8p6fLctra5L1WDeNLRex
   ```

3. **验证连接**：

   在节点 2 上运行以下命令，验证连接是否成功：

   ```powershell
   $env:IPFS_PATH="C:\Apps\.ipfs_node2"
   .\ipfs swarm peers
   ```

   你应该会看到节点 1 的多地址，类似于以下输出：

   ```plaintext
   /ip4/127.0.0.1/tcp/4001/p2p/12D3KooWBUysoAjQjwne3ua8uki4tL6A8p6fLctra5L1WDeNLRex
   ```
