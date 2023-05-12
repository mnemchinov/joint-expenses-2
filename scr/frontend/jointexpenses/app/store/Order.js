Ext.define('JointExpenses.store.Order', {
    extend: 'Ext.data.Store',
    alias: 'store.order',
    model: 'JointExpenses.model.Order',
    data: {
        items: [
            {
                id: 1,
                date: '2023-01-01T13:36:43',
                status: 'Выполнен',
                amount: 2100
            },
            {
                id: 2,
                date: '2023-02-07T10:26:33',
                status: 'Выполнен',
                amount: 2300
            },
            {
                id: 3,
                date: '2023-03-05T11:55:25',
                status: 'Выполнен',
                amount: 2100
            },
            {
                id: 4,
                date: '2023-04-03T16:43:51',
                status: 'Выполнен',
                amount: 2500
            },
            {
                id: 5,
                date: '2023-05-05T13:12:42',
                status: 'Распределение',
                amount: 1500
            },
        ]
    },

    proxy: {
        type: 'ajax',
        url: 'http://127.0.0.1:8000/api/v1/orders',
        reader: {
            type: 'json',
            root: 'data'
        }
    },
    autoLoad: true
});
