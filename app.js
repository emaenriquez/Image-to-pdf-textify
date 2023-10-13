const imageInput = document.getElementById('imageInput');
        const convertButton = document.getElementById('convertButton');
        const downloadButton = document.getElementById('downloadButton');
        const imageContainer = document.getElementById('imageContainer');
        const imagePreview = document.getElementById('imagePreview');

        let imageData = null;

        imageInput.addEventListener('change', function () {
            const selectedFile = imageInput.files[0];
            const reader = new FileReader();

            reader.onload = function () {
                imageData = reader.result;
                imagePreview.src = imageData;

                imageContainer.style.display = 'block';
                downloadButton.style.display = 'block';
            };

            reader.readAsDataURL(selectedFile);
        });

        downloadButton.addEventListener('click', function () {
            if (imageData) {
                const pdf = new jsPDF();
                pdf.addImage(imageData, 'JPEG', 10, 10, 100, 100); // Ajusta las coordenadas y dimensiones según tus necesidades
                pdf.save('imagen_a_pdf.pdf');
            }
        });