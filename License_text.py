from tkinter import *


def openNewWindow(Main):
    newWindow = Toplevel(Main)
    newWindow.geometry("800x500")
    newWindow.configure(bg='#252526')

    License_Text = '''
    ANGELO NICOLI - MIT LICENSE
    
    MIT License
    Copyright (c) 2024 Angelo_Nicoli (Gengio)

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

    PYTHON LICENSE 

    1. This LICENSE AGREEMENT is between the Python Software Foundation ("PSF"), and
    the Individual or Organization ("Licensee") accessing and otherwise using Python
    3.12.3 software in source or binary form and its associated documentation.

    2. Subject to the terms and conditions of this License Agreement, PSF hereby
    grants Licensee a nonexclusive, royalty-free, world-wide license to reproduce,
    analyze, test, perform and/or display publicly, prepare derivative works,
    distribute, and otherwise use Python 3.12.3 alone or in any derivative
    version, provided, however, that PSF's License Agreement and PSF's notice of
    copyright, i.e., "Copyright © 2001-2023 Python Software Foundation; All Rights
    Reserved" are retained in Python 3.12.3 alone or in any derivative version
    prepared by Licensee.

    3. In the event Licensee prepares a derivative work that is based on or
    incorporates Python 3.12.3 or any part thereof, and wants to make the
    derivative work available to others as provided herein, then Licensee hereby
    agrees to include in any such work a brief summary of the changes made to Python
    3.12.3.

    4. PSF is making Python 3.12.3 available to Licensee on an "AS IS" basis.
    PSF MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED.  BY WAY OF
    EXAMPLE, BUT NOT LIMITATION, PSF MAKES NO AND DISCLAIMS ANY REPRESENTATION OR
    WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE
    USE OF PYTHON 3.12.3 WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

    5. PSF SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF PYTHON 3.12.3
    FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A RESULT OF
    MODIFYING, DISTRIBUTING, OR OTHERWISE USING PYTHON 3.12.3, OR ANY DERIVATIVE
    THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.

    6. This License Agreement will automatically terminate upon a material breach of
    its terms and conditions.

    7. Nothing in this License Agreement shall be deemed to create any relationship
    of agency, partnership, or joint venture between PSF and Licensee.  This License
    Agreement does not grant permission to use PSF trademarks or trade name in a
    trademark sense to endorse or promote products or services of Licensee, or any
    third party.

    8. By copying, installing or otherwise using Python 3.12.3, Licensee agrees
    to be bound by the terms and conditions of this License Agreement.
    '''  
    e = Text(newWindow, bg="#3e3e42",fg='white', width =90)

    e.insert(END,License_Text)
    e.grid(row=0, column=0, padx = 10, pady=5, ipady=10, sticky= W+E+S+N)




