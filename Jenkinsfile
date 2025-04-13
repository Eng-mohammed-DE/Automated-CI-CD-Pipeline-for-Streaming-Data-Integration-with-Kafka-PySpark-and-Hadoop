pipeline {
    agent any

    stages {
        stage('Create Virtual Environment') {
            steps {
                script {
                    echo '🔨 Creating Virtual Environment...'
                    sh 'python3 -m venv /home/eng-mohammed/master_node/venv'
                    echo '✅ Virtual Environment Created.'
                }
            }
        }
    }
}
