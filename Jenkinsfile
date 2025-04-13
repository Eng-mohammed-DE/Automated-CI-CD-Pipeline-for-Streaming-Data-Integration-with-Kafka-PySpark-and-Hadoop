pipeline {
    agent any

    environment {
        // Point to the pre-created virtual environment's activate script
        VENV_PATH = '/home/eng-mohammed/master_node/venv/bin/activate'
    }

    stages {
        stage('Verify Virtual Environment') {
            steps {
                script {
                    sh '''
                        echo "📦 Checking Virtual Environment..."
                        . ${VENV_PATH}
                        which python
                        python --version
                        which pip
                        pip --version
                    '''
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Activate and install dependencies; the venv is already in place.
                    sh '. ${VENV_PATH} && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Kafka Producer') {
            steps {
                script {
                    // Activate the venv and run the producer
                    sh '. ${VENV_PATH} && python producer.py'
                }
            }
        }

        stage('Run Spark Consumer') {
            steps {
                script {
                    // Activate the venv and run the Spark consumer
                    sh '. ${VENV_PATH} && spark-submit --master local[*] consumer.py'
                }
            }
        }

        stage('Clean Up') {
            steps {
                echo '🧹 Cleaning up...'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline ran successfully.'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
}
