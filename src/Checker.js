import React from 'react'

const r = Math.sqrt(3)
class Checker extends React.Component {
	
  render() {
		let color1 = this.props.color
		let color2 = this.props.color
		//let color1 = "#123456"
		//let color2 = "#abcdef"
		console.log(this.props.color)
		console.log(color1, color2)
    return (<svg>
      <defs>
				<filter id="outershadow">
					<feDropShadow
						dx=".1"
						dy=".1"
						stdDeviation="0.05"
						flood-opacity=".8"
					/>
				</filter>
      </defs>
      <circle
        style={{
					fill: this.props.color,
          filter:'url(#outershadow)'
        }}
        cx={`calc(16 + ${this.props.x*this.props.scale})`} 
        cy={`calc(18 + ${this.props.y*r*this.props.scale})`} 
        r={`${.8 * this.props.scale}`}

      >
      </circle>
    </svg>)
  }
}

export default Checker