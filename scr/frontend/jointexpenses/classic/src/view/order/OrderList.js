Ext.define('JointExpenses.view.main.List', {
    extend: 'Ext.grid.Panel',
    xtype: 'orderlist',

    requires: [
        'JointExpenses.store.Order'
    ],

    iconCls: 'x-fa fa-archive',
    title: 'Заказы',

    store: {
        type: 'order'
    },

    columns: [
        {
            text: 'Заказ',
            xtype: 'templatecolumn',
            tpl: 'Заказ №{id} от {date:date("d.m.Y H:i:s")}',
            flex: 2
        },
        {text: 'Номер', dataIndex: 'id', flex: 1},
        {
            text: 'Дата',
            dataIndex: 'date',
            xtype: 'datecolumn',
            format: 'd.m.Y H:i:s',
            flex: 1
        },
        {text: 'Статус', dataIndex: 'status', flex: 1},
        {text: 'Сумма', dataIndex: 'amount', xtype: 'numbercolumn', flex: 1},
    ],

    // listeners: {
    //     select: 'onItemSelected'
    // },

    bbar: Ext.create('Ext.PagingToolbar', {
        store: {
            type: 'order'
        }
    }),

    dockedItems: [{
        xtype: 'toolbar',
        items: [{
            iconCls: 'fa fa-plus-circle',
            text: 'Добавить',
            scope: this,
            // handler: this.onAddClick
        }, {
            iconCls: 'fa fa-trash',
            text: 'Удалить',
            disabled: true,
            itemId: 'delete',
            scope: this,
            // handler: this.onDeleteClick
        }]
    }],
    onSelectChange: function (selModel, selections) {
        this.down('#delete').setDisabled(selections.length === 0);
    },
});
grid.getSelectionModel().on('selectionchange', function (selModel, selections) {
    grid.down('#delete').setDisabled(selections.length === 0);
});