# MCP Server для поиска файлов на диске

## Описание:
Этот MCP-сервер позволяет искать файлы по фрагменту пути и возвращать информацию о них в формате JSON.

## Установка и запуск:
В терминал вводим команду вида: python mcp_server.py <Фрагмент пути> <Имя файла>

## Пример промпта:
python mcp_server.py C:\Users\KARABOGAZGOLULTRA\AppData GitHubDesktop

## Пример вывода:
[
  {
    "filename": "GitHubDesktop.exe",
    "path": "C:\\Users\\KARABOGAZGOL\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe",
    "size": 401368,
    "created_at": "2025-03-02T15:35:31.204617"
  },
  {
    "filename": "GitHubDesktop.exe",
    "path": "C:\\Users\\KARABOGAZGOL\\AppData\\Local\\GitHubDesktop\\app-3.4.17\\GitHubDesktop.exe",
    "size": 190721496,
    "created_at": "2025-03-02T15:35:29.900965"
  },
  {
    "filename": "GitHubDesktop-3.4.17-full.nupkg",
    "path": "C:\\Users\\KARABOGAZGOL\\AppData\\Local\\GitHubDesktop\\packages\\GitHubDesktop-3.4.17-full.nupkg",
    "size": 172277786,
    "created_at": "2025-03-02T15:35:29.440505"
  }
]