# start-all.ps1
# Levanta el backend en una ventana nueva
Write-Host "Iniciando backend"
Start-Process powershell -ArgumentList '-NoExit', '-Command', 'cd backend; .\venv\Scripts\Activate.ps1; python app.py'

# Dale unos segundos para que el backend arranque
Start-Sleep -Seconds 5

# Levanta el frontend en otra ventana nueva
Write-Host "Iniciando frontend"
Start-Process powershell -ArgumentList '-NoExit', '-Command', 'cd frontend; npm run dev'

# Dale unos segundos para que Vite arranque
Start-Sleep -Seconds 5

# Abre automáticamente las dos URLs en tu navegador por defecto
Write-Host "Abriendo navegador"
Start-Process "http://127.0.0.1:5000/graphql"
Start-Process "http://localhost:5173"
