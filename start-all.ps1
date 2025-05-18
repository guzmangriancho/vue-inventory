# backend
Write-Host "Iniciando backend"
Start-Process powershell -ArgumentList '-NoExit', '-Command', 'cd backend; .\venv\Scripts\Activate.ps1; python app.py'

# Dale unos segundos para que el backend arranque
Start-Sleep -Seconds 5

# frontend
Write-Host "Iniciando frontend"
Start-Process powershell -ArgumentList '-NoExit', '-Command', 'cd frontend; npm run dev'

Start-Sleep -Seconds 5

Write-Host "Abriendo en navegador"
Start-Process "http://127.0.0.1:5000/graphql"
Start-Process "http://localhost:5173"
