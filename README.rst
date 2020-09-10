.. soc-test README

   Section heading notes:
   # with overline, for parts
   * with overline, for chapters
   =, for sections
   -, for subsections
   ^, for subsubsections
   ", for paragraphs

####################
SoC Test Environment
####################

*****
Goals
*****

* Create a unified environment for testing SoC designs that is reusable for both pre and post silicon
* Use standard tools and frameworks e.g. pytest, cocotb
* Use pytest fixtures to provide/setup & teardown either the simulator environment (cocotb) or the validation hardware environment to the testcase

*****************
Setup Environment
*****************

#. Create a Python virtualenv

.. tabs::

   .. group-tab:: Commands

      ::

         python3 -m venv .venv

   .. group-tab:: Shell Output
                  
      .. code-block:: shell-session

         $python3 -m venv .venv
         DONE
         DONE

         
