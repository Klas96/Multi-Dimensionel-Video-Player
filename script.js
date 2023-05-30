window.addEventListener('DOMContentLoaded', () => {
    const video = document.getElementById('video');
    const contrastRange = document.getElementById('contrast-range');
    const grayscaleRange = document.getElementById('grayscale-range');
    const hueRotateRange = document.getElementById('hue-rotate-range');
    const mirrorButton = document.getElementById('mirror-button');
  
    contrastRange.addEventListener('input', () => {
      const contrastValue = contrastRange.value;
      video.style.filter = `contrast(${contrastValue}%) grayscale(${grayscaleRange.value}%) hue-rotate(${hueRotateRange.value}deg)`;
    });
  
    grayscaleRange.addEventListener('input', () => {
      const grayscaleValue = grayscaleRange.value;
      video.style.filter = `contrast(${contrastRange.value}%) grayscale(${grayscaleValue}%) hue-rotate(${hueRotateRange.value}deg)`;
    });
  
    hueRotateRange.addEventListener('input', () => {
      const hueRotateValue = hueRotateRange.value;
      video.style.filter = `contrast(${contrastRange.value}%) grayscale(${grayscaleRange.value}%) hue-rotate(${hueRotateValue}deg)`;
    });

    let isMirrored = false;
    mirrorButton.addEventListener('click', () => {
        isMirrored = !isMirrored;
        video.style.transform = isMirrored ? 'scaleX(-1)' : 'scaleX(1)';
    });
    
  });
  