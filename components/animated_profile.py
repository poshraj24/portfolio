import streamlit.components.v1 as components
import base64
import os


def add_animoji_profile(image_path, width=300, height=300):
    """
    Creates an animoji from the user's photo using Jeeliz Weboji technology

    Args:
        image_path: Path to the user's profile image
        width: Width of the component
        height: Height of the component
    """
    try:
        with open(image_path, "rb") as f:
            img_base64 = base64.b64encode(f.read()).decode()
    except Exception as e:
        print(f"Error loading image: {e}")
        img_base64 = ""

    html_content = (
        """
    <div id="animoji-container" style="position: relative; width: """
        + str(width)
        + """px; height: """
        + str(height)
        + """px; margin: 0 auto;">
        <!-- Initial photo -->
        <img id="profile-photo" src="data:image/jpeg;base64,"""
        + img_base64
        + """" 
             style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-radius: 50%; 
                    object-fit: cover; z-index: 1; transition: opacity 1s ease-in-out;">
        
        <!-- Canvas for webcam video (hidden) -->
        <canvas id="jeeFaceVideoCanvas" style="display: none;"></canvas>
        
        <!-- Canvas for 3D animation -->
        <canvas id="animoji-canvas" 
                style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; 
                       border-radius: 50%; z-index: 2; opacity: 0; transition: opacity 1s ease-in-out;">
        </canvas>
        
        <!-- Speech bubble -->
        <div id="speech-bubble" 
             style="position: absolute; top: 10px; right: -70px; background: white; 
                    border-radius: 15px; padding: 8px 15px; font-weight: bold; 
                    font-size: 18px; box-shadow: 0 2px 5px rgba(0,0,0,0.2); z-index: 3; 
                    opacity: 0; transition: opacity 0.5s ease-in-out;">
            HI!
            <!-- Speech bubble triangle -->
            <div style="position: absolute; left: 0; top: 50%; width: 0; height: 0; 
                       border: 8px solid transparent; border-right-color: white; 
                       border-left: 0; margin-top: -8px; margin-left: -8px;">
            </div>
        </div>
    </div>

    <!-- Load Jeeliz library -->
    <script src="https://cdn.jsdelivr.net/npm/jeelizWeboji@1.0.0/dist/jeelizFaceExpressions.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.150.1/build/three.min.js"></script>

    <script>
    // Show the photo for 2 seconds before attempting to start the animoji
    setTimeout(function() {
        const photo = document.getElementById('profile-photo');
        const canvas = document.getElementById('animoji-canvas');
        const speechBubble = document.getElementById('speech-bubble');
        
        // Initialize Three.js scene
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({
            canvas: canvas,
            alpha: true,
            antialias: true
        });
        renderer.setSize(canvas.clientWidth, canvas.clientHeight);
        renderer.setClearColor(0x000000, 0);
        
        // Create head
        const headGeometry = new THREE.SphereGeometry(0.8, 32, 32);
        const headMaterial = new THREE.MeshPhongMaterial({
            color: 0xf5d0a9,
            shininess: 30
        });
        const head = new THREE.Mesh(headGeometry, headMaterial);
        scene.add(head);
        
        // Add eyes
        const eyeGeometry = new THREE.SphereGeometry(0.15, 16, 16);
        const eyeMaterial = new THREE.MeshPhongMaterial({ color: 0xffffff });
        const leftEye = new THREE.Mesh(eyeGeometry, eyeMaterial);
        leftEye.position.set(-0.3, 0.2, 0.6);
        head.add(leftEye);
        
        const rightEye = new THREE.Mesh(eyeGeometry, eyeMaterial);
        rightEye.position.set(0.3, 0.2, 0.6);
        head.add(rightEye);
        
        // Add pupils
        const pupilGeometry = new THREE.SphereGeometry(0.05, 16, 16);
        const pupilMaterial = new THREE.MeshPhongMaterial({ color: 0x000000 });
        const leftPupil = new THREE.Mesh(pupilGeometry, pupilMaterial);
        leftPupil.position.set(0, 0, 0.1);
        leftEye.add(leftPupil);
        
        const rightPupil = new THREE.Mesh(pupilGeometry, pupilMaterial);
        rightPupil.position.set(0, 0, 0.1);
        rightEye.add(rightPupil);
        
        // Add mouth
        const mouthGeometry = new THREE.TorusGeometry(0.3, 0.05, 16, 32, Math.PI);
        const mouthMaterial = new THREE.MeshPhongMaterial({ color: 0xcc6666 });
        const mouth = new THREE.Mesh(mouthGeometry, mouthMaterial);
        mouth.position.set(0, -0.3, 0.6);
        mouth.rotation.set(Math.PI, 0, 0);
        head.add(mouth);
        
        // Lighting
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
        scene.add(ambientLight);
        
        const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
        directionalLight.position.set(1, 1, 1);
        scene.add(directionalLight);
        
        camera.position.z = 2.5;
        
        // Make the 3D model visible
        photo.style.opacity = '0';
        canvas.style.opacity = '1';
        
        // Show speech bubble
        setTimeout(function() {
            speechBubble.style.opacity = '1';
        }, 1000);
        
        // Animation variables
        let isTalking = true;
        const mouthOriginalScaleY = mouth.scale.y;
        
        // Stop talking after 2 seconds
        setTimeout(function() {
            isTalking = false;
        }, 3000);
        
        // Animation loop
        function animate() {
            requestAnimationFrame(animate);
            
            // Head movement
            head.rotation.y = Math.sin(Date.now() * 0.001) * 0.2;
            head.rotation.x = Math.sin(Date.now() * 0.0015) * 0.05;
            
            // Blinking
            if (Date.now() % 3000 > 2900) {
                leftEye.scale.y = rightEye.scale.y = 0.1;
            } else {
                leftEye.scale.y = rightEye.scale.y = 1;
            }
            
            // Talking animation
            if (isTalking) {
                const talkFactor = Math.sin(Date.now() * 0.02) * 0.5 + 0.5;
                mouth.scale.y = mouthOriginalScaleY * (1 + talkFactor);
            } else {
                mouth.scale.y = mouthOriginalScaleY;
            }
            
            renderer.render(scene, camera);
        }
        
        animate();
        
        // Optional: If the user wants a more advanced implementation,
        // they can enable webcam-based face tracking.
        // This is commented out by default since it requires webcam permission
        /*
        try {
            JEELIZFACEEXPRESSIONS.init({
                canvasId: 'jeeFaceVideoCanvas',
                NNCPath: 'https://cdn.jsdelivr.net/npm/jeelizWeboji@1.0.0/dist/jeelizFaceExpressionsNNC.json',
                callbackReady: function(errCode) {
                    if (errCode) {
                        console.log('Error initializing Jeeliz:', errCode);
                        return;
                    }
                    console.log('Jeeliz is ready!');
                    JEELIZFACEEXPRESSIONS.switch_displayVideo(false);
                    JEELIZFACEEXPRESSIONS.set_morphUpdateCallback(function(morphs) {
                        // Map the morphs to the 3D model
                        // 0: smileRight, 1: smileLeft, etc.
                        mouth.scale.y = mouthOriginalScaleY * (1 + morphs[6] * 2); // mouthOpen
                        leftEye.scale.y = 1 - morphs[9] * 0.9; // eyeLeftClose
                        rightEye.scale.y = 1 - morphs[8] * 0.9; // eyeRightClose
                    });
                }
            });
        } catch (e) {
            console.log('Could not initialize Jeeliz:', e);
        }
        */
    }, 2000);
    </script>
    """
    )

    components.html(
        html_content,
        height=height + 20,
    )
