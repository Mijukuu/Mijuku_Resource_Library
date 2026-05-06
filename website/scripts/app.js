async function loadData() {
    try {
        const response = await fetch('../../data/generated/all-notes.json')
        if (!response.ok) throw new Error('Failed to load notes data.')
        const data = await response.json();
        console.log(data);

    } catch (error) {
        console.error('Error:', error);
    }
}

loadData();
console.log("app.js loaded");
