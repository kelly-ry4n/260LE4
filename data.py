from __future__ import division

thermister_chart =  [[ 21.736, 61 ],
                     [ 20.919, 62 ],
                     [ 17.980, 66 ],
                     [ 17.321, 67 ],
                     [ 11.223, 79 ],
                     [ 10.837, 80 ],
                     [ 5.9361 , 98 ],
                     [ 5.7492 , 99 ],
                     [ 4.0829 , 110],
                     [ 3.9611 , 111],
                    ]
thermister_chart.reverse()

def slope (x1, x2, y1, y2):
    x2 = (x2 - x1)
    y2 = (y2 - y1)

    m = (y2/x2)
    return m

def intercept(x1, x2, y1, y2):
    m = slope(x1,y1,x2,y2)
    b = y2 - (m*x2)
    return b 

def linear_interpolate(x1,x2,y1,y2,t):
    from scipy.interpolate import interp1d

    linear =  interp1d([x1,x2], [y1,y2])

    print x1,x2, t

    return linear(t)


def thermister_converter(t):

    for i in xrange(len(thermister_chart)):
        if t <= thermister_chart[i][0]:
            index = i
            break
    else:
        print "SOMETHING FUCKED UP THERE IS NO THERMISTER VALUE FOR THIS"

    x1 = thermister_chart[index - 1][0]
    y1 = thermister_chart[index - 1][1]
    x2 = thermister_chart[index][0]
    y2 = thermister_chart[index][1]


    return linear_interpolate(x1,x2,y1,y2, t)

print thermister_converter(4.002)

    


## E1

e1_thermister_ucert = 0.005 # kiloohm
e1_probe_ucert      = 0.01  #mC
   # power
   #   -   black
   #   -   -       polished
   #   -   -       -       dull
   #   -   -       -       -   white
   #   -   -       -       -   -       thermister   
e1 = [[ 9  ,21.36, 1.42, 3.96, 20.32, 4.002],
      [ 8.5,20.91, 1.27, 3.75, 19.70, 4.062],
      [ 7.5,16.87, 1.07, 3.04, 16.55, 5.806],
      [ 5.5,11.35, 0.76, 2.26, 11.19, 11.09],
      [ 4  ,6.86 , 0.64, 1.30, 6.75 , 21.40]]
glass= [ 9 ,0    ,0.05 , 0.05, 0.03 , 4.002] ## at 5 cm
nglass=[ 9 ,17.42,1.03 , 2.97, 2.97 , 17.45]







## E2


rref       = 0.4990 #Ohm
rref_ucert = 0.0002

sensor_to_filiment_distance = 2.4990 #cm
sensor_to_filiment_distance_ucert = 0.0002

## The reference measurements along the track for background
          # distance
          # -      1st measurement
          # -       -    2nd measurement
e2_ref = [[ 2.4 , 0.02, -0.24],
          [ 12.4, 0.01, -0.22],
          [ 22.4, 0.01, -0.22],
          [ 32.4, 0.06, -0.3 ],
          [ 42.4, 0.03, -0.22], 
          [ 52.4, 0.05, -21.0],
          [ 62.4, 0.03, -0.41],
          [ 72.4, 0.04, -0.41],
          [ 82.4, 0.03, -0.38],
          [ 92.4, 0.03, -0.29]
      ]

## The sensor measurements with the light on

#  distance   reading (mV)    
e2 = [[ 2.4 , 142.71],
      [ 4.9 , 44.03 ],
      [ 7.4 , 20.96 ],
      [ 9.9 , 11.24 ],
      [ 12.4, 7.21  ],
      [ 14.9, 5.10  ],
      [ 17.4, 3.89  ],
      [ 19.9, 3.04  ],
      [ 24.4, 1.96  ],
      [ 29.9, 1.26  ],
      [ 34.9, 0.90  ],
      [ 39.9, 0.59  ],
      [ 44.9, 0.34  ],
      [ 49.9, 0.25  ],
      [ 54.9, 0.16  ],
      [ 59.9, 0.06  ],
      [ 64.9, 0.03  ],
      [ 69.9, 0.03  ],
      [ 74.9, -0.11 ],
      [ 79.9, -0.16 ],
      [ 84.9, -0.10 ],
      [ 89.9, -0.13 ],
      [ 94.9, -0.13 ],
      [ 99.9, -0.16 ]
]

## Last Part

ambient_temps = [25.3, 24.7, 25.8, 25.1, 25.4]

    # Voltage (V)
    #     -   Amp (amps)
    #     -   -       sensor reading (mV)
    #     -   -       -       background (mV)
e3 = [[ 1.000, 0.857, -0.1,  0    ],
      [ 2.033, 1.108, 0.53,  0    ],
      [ 2.998, 1.316, 1.53,  0.01 ],
      [ 4.081, 1.523, 3.07,  0    ],
      [ 5.072, 1.696, 4.79,  0.02 ],
      [ 5.995, 1.846, 6.61,  0.06 ],
      [ 7.00 , 1.999, 8.75,  0.07 ],
      [ 8.01 , 2.141, 11.17, 0.17 ],
      [ 9.00 , 2.273, 13.72, 0.28 ],
      [ 10.10, 2.405, 16.38, 0.38 ],
      [ 10.99, 2.523, 19.15, 0.37 ],
      [ 12.03, 2.649, 22.22, 0.48 ]

      ]