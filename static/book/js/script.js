const availableSlots = [
    "10:00 AM - 11:00 AM",
    "11:00 AM - 12:00 PM",
    "2:00 PM - 3:00 PM",
    "3:00 PM - 4:00 PM",
    "4:00 PM - 5:00 PM",
];

const datepicker = $('#datepicker').datepicker({
    format: 'yyyy-mm-dd',
    todayHighlight: true
}).on('changeDate', function (e) {
    renderAvailableSlots();
});

const availableSlotsContainer = document.getElementById("availableSlots");

// Function to add slots to the available slots container
function renderAvailableSlots() {
    const selectedDate = datepicker.datepicker('getFormattedDate');
    availableSlotsContainer.innerHTML = `<h3>Available Slots for ${selectedDate}</h3>`;
    
    availableSlots.forEach(slot => {
        const slotElement = document.createElement("div");
        slotElement.classList.add("slot");
        slotElement.textContent = slot;
        slotElement.addEventListener("click", () => toggleSlot(slotElement));
        availableSlotsContainer.appendChild(slotElement);
    });
}

// Function to toggle the selection of a slot
function toggleSlot(slotElement) {
    if (slotElement.classList.contains("selected")) {
        slotElement.classList.remove("selected");
    } else {
        slotElement.classList.add("selected");
    }
}

// Initial rendering of available slots
renderAvailableSlots();