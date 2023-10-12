// Инициализация слайдера
const initSlider = () => {
    // Получаем элементы DOM
    const imageList = document.querySelector(".slider-wrapper .image-list"); // Получаем контейнер изображений
    const slideButtons = document.querySelectorAll(".slider-wrapper .slide-button"); // Получаем кнопки переключения слайдов
    const sliderScrollbar = document.querySelector(".container .slider-scrollbar"); // Получаем элемент полосы прокрутки
    const scrollbarThumb = sliderScrollbar.querySelector(".scrollbar-thumb"); // Получаем элемент "бегунок" полосы прокрутки
    const maxScrollLeft = imageList.scrollWidth - imageList.clientWidth; // Максимальная возможная позиция скролла влево

    // Обработка перетаскивания "бегунка" полосы прокрутки
    scrollbarThumb.addEventListener("mousedown", (e) => {
        const startX = e.clientX; // Начальная позиция курсора по горизонтали
        const thumbPosition = scrollbarThumb.offsetLeft; // Текущая позиция "бегунка"
        const maxThumbPosition = sliderScrollbar.getBoundingClientRect().width - scrollbarThumb.offsetWidth; // Максимальная позиция "бегунка"

        // Обновление позиции "бегунка" при перемещении мыши
        const handleMouseMove = (e) => {
            const deltaX = e.clientX - startX; // Изменение позиции курсора по горизонтали
            const newThumbPosition = thumbPosition + deltaX;

            // Гарантия, что "бегунок" останется внутри границ
            const boundedPosition = Math.max(0, Math.min(maxThumbPosition, newThumbPosition));
            const scrollPosition = (boundedPosition / maxThumbPosition) * maxScrollLeft;

            scrollbarThumb.style.left = `${boundedPosition}px`; // Обновление позиции "бегунка"
            imageList.scrollLeft = scrollPosition; // Обновление позиции скролла изображений
        }

        // Удаление обработчиков событий при отпускании кнопки мыши
        const handleMouseUp = () => {
            document.removeEventListener("mousemove", handleMouseMove);
            document.removeEventListener("mouseup", handleMouseUp);
        }

        // Добавление обработчиков событий для взаимодействия с перетаскиванием
        document.addEventListener("mousemove", handleMouseMove);
        document.addEventListener("mouseup", handleMouseUp);
    });

    // Переключение изображений при клике на кнопки слайдов
    slideButtons.forEach(button => {
        button.addEventListener("click", () => {
            const direction = button.id === "prev-slide" ? -1 : 1;
            const scrollAmount = imageList.clientWidth * direction;
            imageList.scrollBy({ left: scrollAmount, behavior: "smooth" });
        });
    });

    // Отображение или скрытие кнопок слайдов в зависимости от позиции скролла
    const handleSlideButtons = () => {
        slideButtons[0].style.display = imageList.scrollLeft <= 0 ? "none" : "flex";
        slideButtons[1].style.display = imageList.scrollLeft >= maxScrollLeft ? "none" : "flex";
    }

    // Обновление позиции "бегунка" полосы прокрутки на основе позиции скролла изображений
    const updateScrollThumbPosition = () => {
        const scrollPosition = imageList.scrollLeft;
        const thumbPosition = (scrollPosition / maxScrollLeft) * (sliderScrollbar.clientWidth - scrollbarThumb.offsetWidth);
        scrollbarThumb.style.left = `${thumbPosition}px`;
    }

    // Вызов этих двух функций при прокрутке списка изображений
    imageList.addEventListener("scroll", () => {
        updateScrollThumbPosition();
        handleSlideButtons();
    });
}

// Вызов функции при изменении размера окна и после загрузки страницы
window.addEventListener("resize", initSlider);
window.addEventListener("load", initSlider);
