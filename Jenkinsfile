pipeline {
    agent any

    environment {
        VENV_PATH = '/home/eng-mohammed/master_node/venv'
        WORKSPACE_PATH = '/var/jenkins_home/workspace/master_job'
    }

    stages {
        stage('List Files in Workspace') {
            steps {
                script {
                    echo 'Listing files in the workspace...'
                    sh 'ls -la $WORKSPACE_PATH'
                }
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                script {
                    echo 'Setting up virtual environment...'
                    // Ensure virtual environment is set up
                    sh 'python3 -m venv $VENV_PATH || true'
                    sh '$VENV_PATH/bin/pip install -r $WORKSPACE_PATH/requirements.txt'
                }
            }
        }

        stage('Run Producer') {
            steps {
                script {
                    try {
                        echo 'Running producer.py...'
                        // Activate the virtual environment and run producer.py
                        sh '. $VENV_PATH/bin/activate && python $WORKSPACE_PATH/producer.py'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }

        stage('Run Consumer') {
            steps {
                script {
                    try {
                        echo 'Running consumer.py...'
                        // Activate the virtual environment and run consumer.py
                        sh '. $VENV_PATH/bin/activate && python $WORKSPACE_PATH/consumer.py'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    echo 'Cleaning up...'
                    // Deactivate the virtual environment if necessary
                    sh 'deactivate || true'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'
        }
        success {
            echo 'Pipeline finished successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
