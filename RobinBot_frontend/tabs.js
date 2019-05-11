let activeTab;

function hideTab(tabRoot) {
    tabRoot.style.display = 'none';
}

function showTab(tabRoot) {
    tabRoot.style.display = '';
}

document.addEventListener('DOMContentLoaded', () => {
    activeTab = document.querySelector('.tab-header[data-active="true"]');

    document.querySelectorAll(`.tab-content:not([data-for="${activeTab.id}"])`).forEach(element => hideTab(element));

    document.querySelectorAll('.tab-header').forEach(header => {
        header.addEventListener('click', event => {
            if (event.target.getAttribute('data-active') != 'true') {
                activeTab.setAttribute('data-active', 'false');
                activeTab.innerHTML = activeTab.getAttribute('data-icon');
                hideTab(document.querySelector(`.tab-content[data-for="${activeTab.id}"]`));

                activeTab = event.target;
                activeTab.setAttribute('data-active', 'true');
                activeTab.innerHTML = activeTab.getAttribute('data-text');
                showTab(document.querySelector(`.tab-content[data-for="${activeTab.id}"]`));
            } 
        });
    });
});