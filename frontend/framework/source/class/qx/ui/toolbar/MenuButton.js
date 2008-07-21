/* ************************************************************************

   qooxdoo - the new era of web development

   http://qooxdoo.org

   Copyright:
     2004-2008 1&1 Internet AG, Germany, http://www.1und1.de

   License:
     LGPL: http://www.gnu.org/licenses/lgpl.html
     EPL: http://www.eclipse.org/org/documents/epl-v10.php
     See the LICENSE file in the project's top-level directory for details.

   Authors:
     * Sebastian Werner (wpbasti)
     * Andreas Ecker (ecker)

************************************************************************ */

qx.Class.define("qx.ui.toolbar.MenuButton",
{
  extend : qx.ui.toolbar.Button,




  /*
  *****************************************************************************
     CONSTRUCTOR
  *****************************************************************************
  */

  construct : function(label, icon, menu)
  {
    this.base(arguments, label, icon);

    // Initialize properties
    if (menu != null) {
      this.setMenu(menu);
    }
  },




  /*
  *****************************************************************************
     PROPERTIES
  *****************************************************************************
  */

  properties :
  {
    /** The menu instance to show when clicking on the button */
    menu :
    {
      check : "qx.ui.menu.Menu",
      nullable : true,
      apply : "_applyMenu",
      event : "changeMenu"
    }
  },




  /*
  *****************************************************************************
     MEMBERS
  *****************************************************************************
  */

  members :
  {
    /*
    ---------------------------------------------------------------------------
      PROPERTY APPLY ROUTINES
    ---------------------------------------------------------------------------
    */

    // property apply
    _applyMenu : function(value, old)
    {
      if (old) {
        old.removeListener("changeVisibility", this._onMenuChange, this);
      }

      if (value) {
        value.addListener("changeVisibility", this._onMenuChange, this);
      }
    },




    /*
    ---------------------------------------------------------------------------
      HELPER METHODS
    ---------------------------------------------------------------------------
    */

    /**
     * Positions and shows the attached menu widget.
     *
     * @param selectFirst {Boolean?false} Whether the first menu button should be selected
     */
    open : function(selectFirst)
    {
      var menu = this.getMenu();

      if (menu)
      {
        // Hide all menus first
        qx.ui.menu.Manager.getInstance().hideAll();

        // Show the attached menu
        var pos = this.getContainerLocation();
        menu.moveTo(pos.left, pos.bottom);
        menu.open(this);

        // Select first item
        if (selectFirst)
        {
          var first = menu.getChildren()[0];
          if (first) {
            menu.setHoverItem(first);
          }
        }
      }
    },


    /**
     * Inspects the parent chain to find a ToolBar instance.
     *
     * @return {qx.ui.toolbar.ToolBar} Toolbar instance or <code>null</code>.
     */
    getToolBar : function()
    {
      var parent = this;
      while (parent)
      {
        if (parent instanceof qx.ui.toolbar.ToolBar) {
          return parent;
        }

        parent = parent.getLayoutParent();
      }

      return null;
    },




    /*
    ---------------------------------------------------------------------------
      EVENT LISTENERS
    ---------------------------------------------------------------------------
    */

    /**
     * Listener for visibility property changes of the attached menu
     *
     * @param e {qx.event.type.Data} Property change event
     */
    _onMenuChange : function(e)
    {
      var menu = this.getMenu();
      var toolbar = this.getToolBar();

      if (menu.isVisible())
      {
        this.addState("pressed");

        if (toolbar) {
          toolbar.setOpenMenu(menu);
        }
      }
      else
      {
        this.removeState("pressed");

        if (toolbar && toolbar.getOpenMenu() == menu) {
          toolbar.resetOpenMenu();
        }
      }
    },


    /**
     * Event listener for mousedown event
     *
     * @param e {qx.event.type.Mouse} mousedown event object
     */
    _onMouseDown : function(e)
    {
      var menu = this.getMenu();
      if (menu)
      {
        if (!menu.isVisible())
        {
          this.open();
        }
        else
        {
          menu.exclude();
        }

        // Event is processed, stop it for others
        e.stopPropagation();
      }
    },


    /**
     * Event listener for mouseup event
     *
     * @param e {qx.event.type.Mouse} mouseup event object
     */
    _onMouseUp : function(e)
    {
      // Just stop propagation to stop menu manager from getting the event
      e.stopPropagation();
    },


    /**
     * Event listener for mouseover event
     *
     * @param e {qx.event.type.Mouse} mouseover event object
     */
    _onMouseOver : function(e)
    {
      this.addState("hovered");

      if (this.getMenu())
      {
        var toolbar = this.getToolBar();
        if (toolbar.getOpenMenu())
        {
          // Hide all open menus first
          qx.ui.menu.Manager.getInstance().hideAll();

          // Then show the attached menu
          this.open();
        }
      }
    },


    /**
     * Event listener for mouseout event
     *
     * @param e {qx.event.type.Mouse} mouseout event object
     */
    _onMouseOut : function(e)
    {
      // Just remove the hover state
      this.removeState("hovered");
    }
  }
});
