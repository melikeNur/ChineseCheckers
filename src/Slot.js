import React from 'react'

const r = Math.sqrt(3)

const Slot = ({scale = 1, x, y}) =>
  <svg>
    <defs>
			<filter id="innershadow">
				<feComponentTransfer in="SourceAlpha">
					<feFuncA type="table" tableValues="1 0" />
				</feComponentTransfer>
				<feGaussianBlur stdDeviation=".1"/>
				<feOffset dx=".1" dy=".1" result="offsetblur"/>
				<feFlood flood-color="rgb(20, 0, 0)" result="color"/>
				<feComposite in2="offsetblur" operator="in"/>
				<feComposite in2="SourceAlpha" operator="in" />
				<feMerge>
					<feMergeNode in="SourceGraphic" />
					<feMergeNode />
				</feMerge>
			</filter>
    </defs>
    <circle
      style={{
        fill: '#8A8583',
        filter:'url(#innershadow)'
      }}
      cx={`calc(16 + ${x*scale})`} 
      cy={`calc(18 + ${y*r*scale})`} 
      r={`${.8 * scale}`}

    >
    </circle>
  </svg>

export default Slot