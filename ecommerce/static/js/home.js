function toggleCategory(categoryId) {
    // Hide all categories
    const allCategories = document.querySelectorAll('.category-details');
    allCategories.forEach(category => {
        category.classList.add('hidden');
    });
    
    // Show the selected category
    const selectedCategory = document.getElementById(categoryId);
    if (selectedCategory) {
        selectedCategory.classList.remove('hidden');
    }
}