stage('Create Virtual Environment') {
    steps {
        script {
            echo '🔨 Checking if Virtual Environment exists...'
            
            // Ensure Python is available
            sh 'python3 --version || exit 1'

            // Check if the virtual environment exists; if not, create it
            if (!fileExists('/home/eng-mohammed/master_node/venv/bin/activate')) {
                echo '❌ Virtual Environment not found. Creating it now...'
                // Make sure the venv directory exists, then create the virtual environment
                sh 'mkdir -p /home/eng-mohammed/master_node/venv && python3 -m venv /home/eng-mohammed/master_node/venv'
            } else {
                echo '✅ Virtual Environment already exists.'
            }
        }
    }
}
