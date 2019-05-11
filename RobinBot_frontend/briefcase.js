let activeBtnCurrency;

function updateChart() {
    chart = Highcharts.chart('currency-chart', {
        chart: {
            type: 'line'
        },
        title: {
            text: `${activeBtnCurrency.getAttribute('data-currency')} Rate`
        },
        xAxis: {
            visible: false
        },
        yAxis: {
            title: {
                text: 'Bitcoins per unit'
            }
        },
        series: [{
            name: ``,
            data: [1, 0, 4, 20, -4]
        }]
    });
}

function updateSelectedCurrency(button) {
    activeBtnCurrency.setAttribute('data-active', 'false');

    activeBtnCurrency = button;
    activeBtnCurrency.setAttribute('data-active', 'true');

    updateChart();
}

document.addEventListener('DOMContentLoaded', () => {
    activeBtnCurrency = document.querySelector('.btn-currency[data-active="true"]');

    document.querySelectorAll('.btn-currency').forEach(button => {
        button.addEventListener('click', event => updateSelectedCurrency(event.target));
    });

    document.querySelector('.btn-currency-sum').addEventListener('click', event => updateSelectedCurrency(event.target));

    let chart;
    updateChart();
});