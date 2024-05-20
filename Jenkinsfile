pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository containing the Python script
                git url: 'https://github.com/serhii-sv/sharely-python-test.git', branch: 'master'
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    // Install any dependencies if necessary
                    sh '''
                    if [ ! -d "venv" ]; then
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install -r requirements.txt  # Install Python dependencies
                    fi
                    '''
                }
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    // Run the Python script
                    sh '''
                    source venv/bin/activate
                    python main.py --param1 value1 --param2 value2
                    '''
                }
            }
        }
    }

    post {
        always {
            // Clean up after the build
            cleanWs()
        }
    }
}
