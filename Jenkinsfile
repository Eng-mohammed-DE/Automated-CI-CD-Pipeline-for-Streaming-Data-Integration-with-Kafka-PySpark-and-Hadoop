stage('Check Venv Dependencies') {
    steps {
        script {
            echo '🔍 Verifying that python3.11-venv is installed...'
            sh '''
                if ! python3 -m venv --help > /dev/null 2>&1; then
                    echo "❌ python3.11-venv is not installed!"
                    echo "💡 Run: sudo apt install python3.11-venv"
                    exit 1
                else
                    echo "✅ python3.11-venv is available."
                fi
            '''
        }
    }
}
